"""Data processing module"""

from typing import List, Dict, Any
import statistics
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    """Data processing utilities"""
    
    def flatten_list(self, nested_list: List) -> List:
        """Flatten nested list"""
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(self.flatten_list(item))
            else:
                result.append(item)
        return result
    
    def remove_duplicates(self, items: List) -> List:
        """Remove duplicates from list"""
        return list(dict.fromkeys(items))
    
    def chunk_list(self, items: List, chunk_size: int) -> List[List]:
        """Split list into chunks"""
        return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
    
    def merge_dicts(self, *dicts: Dict) -> Dict:
        """Merge multiple dictionaries"""
        result = {}
        for d in dicts:
            result.update(d)
        return result
    
    def dict_to_list(self, d: Dict) -> List[tuple]:
        """Convert dict to list of tuples"""
        return list(d.items())
    
    def list_to_dict(self, items: List[tuple]) -> Dict:
        """Convert list of tuples to dict"""
        return dict(items)
    
    def filter_by_key(self, data: List[Dict], key: str, value: Any) -> List[Dict]:
        """Filter list of dicts by key-value"""
        return [item for item in data if item.get(key) == value]
    
    def sort_by_key(self, data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        """Sort list of dicts by key"""
        return sorted(data, key=lambda x: x.get(key, ''), reverse=reverse)
    
    def group_by_key(self, data: List[Dict], key: str) -> Dict:
        """Group list of dicts by key"""
        result = {}
        for item in data:
            k = item.get(key)
            if k not in result:
                result[k] = []
            result[k].append(item)
        return result
    
    def get_unique_values(self, data: List[Dict], key: str) -> List:
        """Get unique values for a key"""
        return list(set(item.get(key) for item in data))
    
    def transpose_matrix(self, matrix: List[List]) -> List[List]:
        """Transpose a matrix"""
        return [list(row) for row in zip(*matrix)]
    
    def rotate_list(self, items: List, positions: int) -> List:
        """Rotate list by positions"""
        if not items:
            return items
        positions = positions % len(items)
        return items[-positions:] + items[:-positions]
    
    def demo(self):
        """Demo data processing"""
        nested = [[1, 2], [3, [4, 5]], 6]
        print(f"✓ Flatten {nested}: {self.flatten_list(nested)}")
        
        items = [1, 2, 2, 3, 3, 3, 4]
        print(f"✓ Remove duplicates {items}: {self.remove_duplicates(items)}")
        
        chunked = self.chunk_list([1,2,3,4,5,6], 2)
        print(f"✓ Chunk [1-6] by 2: {chunked}")
        
        d1, d2 = {'a': 1}, {'b': 2}
        print(f"✓ Merge {d1} + {d2}: {self.merge_dicts(d1, d2)}")
        
        data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        filtered = self.filter_by_key(data, 'name', 'Alice')
        print(f"✓ Filter by name=Alice: {filtered}")