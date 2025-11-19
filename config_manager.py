"""Configuration manager module"""

import json
from pathlib import Path
from typing import Any, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class ConfigManager:
    """Configuration management"""
    
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config = self.load()
    
    def load(self) -> Dict:
        """Load configuration"""
        try:
            if Path(self.config_file).exists():
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return {}
    
    def save(self) -> bool:
        """Save configuration"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            logger.info(f"Saved config to {self.config_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def set(self, key: str, value: Any) -> bool:
        """Set configuration value"""
        try:
            keys = key.split('.')
            config = self.config
            for k in keys[:-1]:
                if k not in config:
                    config[k] = {}
                config = config[k]
            config[keys[-1]] = value
            return self.save()
        except Exception as e:
            logger.error(f"Failed to set config: {e}")
            return False
    
    def demo(self):
        """Demo config manager"""
        self.set('app.name', 'BigUtility')
        self.set('app.version', '1.0.0')
        print(f"✓ Set app.name: {self.get('app.name')}")
        print(f"✓ Set app.version: {self.get('app.version')}")
        
        # Cleanup
        Path(self.config_file).unlink(missing_ok=True)