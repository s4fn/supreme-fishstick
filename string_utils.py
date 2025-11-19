"""String utilities module"""

import re
import string
from typing import List
import logging

logger = logging.getLogger(__name__)

class StringUtils:
    """String manipulation utilities"""
    
    def reverse_string(self, text: str) -> str:
        """Reverse a string"""
        return text[::-1]
    
    def capitalize_words(self, text: str) -> str:
        """Capitalize first letter of each word"""
        return ' '.join(word.capitalize() for word in text.split())
    
    def remove_duplicates(self, text: str) -> str:
        """Remove duplicate characters"""
        return ''.join(dict.fromkeys(text))
    
    def is_palindrome(self, text: str) -> bool:
        """Check if string is palindrome"""
        clean = re.sub(r'[^a-z0-9]', '', text.lower())
        return clean == clean[::-1]
    
    def count_vowels(self, text: str) -> int:
        """Count vowels in string"""
        return sum(1 for char in text.lower() if char in 'aeiou')
    
    def count_consonants(self, text: str) -> int:
        """Count consonants in string"""
        return sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
    
    def extract_numbers(self, text: str) -> List[str]:
        """Extract all numbers from string"""
        return re.findall(r'\d+', text)
    
    def extract_emails(self, text: str) -> List[str]:
        """Extract emails from string"""
        return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    
    def remove_special_chars(self, text: str) -> str:
        """Remove special characters"""
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    def slug_format(self, text: str) -> str:
        """Convert to slug format"""
        return re.sub(r'[^\w\s-]', '', text).strip().lower().replace(' ', '-')
    
    def truncate_string(self, text: str, length: int, suffix: str = "...") -> str:
        """Truncate string to length"""
        if len(text) <= length:
            return text
        return text[:length-len(suffix)] + suffix
    
    def is_anagram(self, text1: str, text2: str) -> bool:
        """Check if two strings are anagrams"""
        return sorted(text1.replace(" ", "").lower()) == sorted(text2.replace(" ", "").lower())
    
    def word_frequency(self, text: str) -> dict:
        """Get word frequency"""
        words = text.lower().split()
        return {word: words.count(word) for word in set(words)}
    
    def camel_case(self, text: str) -> str:
        """Convert to camelCase"""
        words = text.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    def snake_case(self, text: str) -> str:
        """Convert to snake_case"""
        return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    
    def demo(self):
        """Demo string utilities"""
        test_str = "Hello World Python"
        print(f"✓ Original: {test_str}")
        print(f"✓ Reversed: {self.reverse_string(test_str)}")
        print(f"✓ Capitalized: {self.capitalize_words(test_str)}")
        print(f"✓ Vowels: {self.count_vowels(test_str)}")
        print(f"✓ Consonants: {self.count_consonants(test_str)}")
        print(f"✓ Slug: {self.slug_format(test_str)}")
        print(f"✓ Word Frequency: {self.word_frequency(test_str)}")
        print(f"✓ Is 'racecar' palindrome? {self.is_palindrome('racecar')}")
        print(f"✓ CamelCase: {self.camel_case(test_str)}")
        print(f"✓ snake_case: {self.snake_case('HelloWorld')}")