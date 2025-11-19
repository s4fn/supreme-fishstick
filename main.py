#!/usr/bin/env python3
"""
BIG Python Utility - A comprehensive utility toolkit with tons of functions
Version: 1.0.0
Author: s4fn
Created: 2025-11-19
"""

import sys
import logging
from pathlib import Path

# Import all modules
from modules.file_operations import FileOps
from modules.data_processing import DataProcessor
from modules.string_utils import StringUtils
from modules.math_utils import MathUtils
from modules.date_time_utils import DateTimeUtils
from modules.system_utils import SystemUtils
from modules.network_utils import NetworkUtils
from modules.crypto_utils import CryptoUtils
from modules.json_utils import JSONUtils
from modules.csv_utils import CSVUtils
from modules.cli_interface import CLIInterface
from modules.config_manager import ConfigManager
from modules.logger_setup import setup_logger

# Setup logging
logger = setup_logger(__name__)

class BigUtility:
    """Main utility class orchestrating all functionality"""
    
    def __init__(self):
        self.file_ops = FileOps()
        self.data_processor = DataProcessor()
        self.string_utils = StringUtils()
        self.math_utils = MathUtils()
        self.date_time_utils = DateTimeUtils()
        self.system_utils = SystemUtils()
        self.network_utils = NetworkUtils()
        self.crypto_utils = CryptoUtils()
        self.json_utils = JSONUtils()
        self.csv_utils = CSVUtils()
        self.config_manager = ConfigManager()
        logger.info("BIG Utility initialized successfully")
    
    def run_cli(self):
        """Run the CLI interface"""
        cli = CLIInterface(self)
        cli.run()
    
    def demo_all_features(self):
        """Demo all features"""
        print("\n" + "="*60)
        print("BIG PYTHON UTILITY - FEATURE DEMONSTRATION")
        print("="*60 + "\n")
        
        # File Operations
        print("[1/11] FILE OPERATIONS")
        print("-" * 40)
        self.file_ops.demo()
        
        # String Utils
        print("\n[2/11] STRING UTILITIES")
        print("-" * 40)
        self.string_utils.demo()
        
        # Math Utils
        print("\n[3/11] MATH UTILITIES")
        print("-" * 40)
        self.math_utils.demo()
        
        # Date/Time Utils
        print("\n[4/11] DATE/TIME UTILITIES")
        print("-" * 40)
        self.date_time_utils.demo()
        
        # Data Processing
        print("\n[5/11] DATA PROCESSING")
        print("-" * 40)
        self.data_processor.demo()
        
        # System Utils
        print("\n[6/11] SYSTEM UTILITIES")
        print("-" * 40)
        self.system_utils.demo()
        
        # Network Utils
        print("\n[7/11] NETWORK UTILITIES")
        print("-" * 40)
        self.network_utils.demo()
        
        # Crypto Utils
        print("\n[8/11] CRYPTO UTILITIES")
        print("-" * 40)
        self.crypto_utils.demo()
        
        # JSON Utils
        print("\n[9/11] JSON UTILITIES")
        print("-" * 40)
        self.json_utils.demo()
        
        # CSV Utils
        print("\n[10/11] CSV UTILITIES")
        print("-" * 40)
        self.csv_utils.demo()
        
        # Config Manager
        print("\n[11/11] CONFIG MANAGEMENT")
        print("-" * 40)
        self.config_manager.demo()
        
        print("\n" + "="*60)
        print("DEMONSTRATION COMPLETE!")
        print("="*60 + "\n")

def main():
    """Main entry point"""
    utility = BigUtility()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            utility.demo_all_features()
        elif sys.argv[1] == "--cli":
            utility.run_cli()
        else:
            print("Usage: python main.py [--demo|--cli]")
    else:
        utility.demo_all_features()

if __name__ == "__main__":
    main()