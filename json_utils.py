"""JSON utilities module"""

import json
from typing import Any, Dict, List
import logging

logger = logging.getLogger(__name__)

class JSONUtils:
    """JSON utilities"""
    
    def to_json(self, obj: Any, indent: int = 2) -> str:
        """Convert object to JSON string"""
        try:
            return json.dumps(obj, indent=indent)
        except Exception as e:
            logger.error(f"Failed to convert to JSON: {e}")
            return ""
    
    def from_json(self, json_str: str) -> Any:
        """Parse JSON string"""
        try:
            return json.loads(json_str)
        except Exception as e:
            logger.error(f"Failed to parse JSON: {e}")
            return None
    
    def save_json(self, filepath: str, data: Any) -> bool:
        """Save data to JSON file"""
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved JSON to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to save JSON: {e}")
            return False
    
    def load_json(self, filepath: str) -> Any:
        """Load data from JSON file"""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load JSON: {e}")
            return None
    
    def is_valid_json(self, json_str: str) -> bool:
        """Check if string is valid JSON"""
        try:
            json.loads(json_str)
            return True
        except:
            return False
    
    def pretty_print_json(self, json_str: str) -> str:
        """Pretty print JSON"""
        try:
            obj = json.loads(json_str)
            return json.dumps(obj, indent=2)
        except:
            return ""
    
    def demo(self):
        """Demo JSON utilities"""
        data = {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'coding']}
        json_str = self.to_json(data)
        print(f"✓ To JSON: {json_str.split(chr(10))[0]}...")
        parsed = self.from_json(json_str)
        print(f"✓ From JSON: {parsed}")
        print(f"✓ Is valid JSON: {self.is_valid_json(json_str)}")