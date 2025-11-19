"""CSV utilities module"""

import csv
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class CSVUtils:
    """CSV utilities"""
    
    def read_csv(self, filepath: str) -> List[Dict]:
        """Read CSV file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except Exception as e:
            logger.error(f"Failed to read CSV: {e}")
            return []
    
    def write_csv(self, filepath: str, data: List[Dict], fieldnames: List[str] = None) -> bool:
        """Write to CSV file"""
        try:
            if not data:
                return False
            
            if fieldnames is None:
                fieldnames = list(data[0].keys())
            
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            logger.info(f"Saved CSV to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to write CSV: {e}")
            return False
    
    def get_column(self, data: List[Dict], column: str) -> List:
        """Get column from CSV data"""
        return [row.get(column) for row in data]
    
    def filter_csv(self, data: List[Dict], key: str, value: str) -> List[Dict]:
        """Filter CSV data"""
        return [row for row in data if row.get(key) == value]
    
    def demo(self):
        """Demo CSV utilities"""
        data = [
            {'name': 'Alice', 'age': '30'},
            {'name': 'Bob', 'age': '25'},
            {'name': 'Charlie', 'age': '35'}
        ]
        
        filepath = 'test_data.csv'
        self.write_csv(filepath, data)
        print(f"✓ Created CSV with {len(data)} rows")
        
        loaded = self.read_csv(filepath)
        print(f"✓ Loaded {len(loaded)} rows from CSV")
        
        names = self.get_column(loaded, 'name')
        print(f"✓ Names column: {names}")
        
        # Cleanup
        import os
        os.remove(filepath)