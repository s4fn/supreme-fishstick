"""Math utilities module"""

import math
from typing import List, Union
import logging

logger = logging.getLogger(__name__)

class MathUtils:
    """Mathematical utilities"""
    
    def factorial(self, n: int) -> int:
        """Calculate factorial"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        return math.factorial(n)
    
    def fibonacci(self, n: int) -> List[int]:
        """Generate fibonacci sequence"""
        if n <= 0:
            return []
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    
    def is_prime(self, n: int) -> bool:
        """Check if number is prime"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def gcd(self, a: int, b: int) -> int:
        """Calculate greatest common divisor"""
        return math.gcd(a, b)
    
    def lcm(self, a: int, b: int) -> int:
        """Calculate least common multiple"""
        return abs(a * b) // math.gcd(a, b)
    
    def power(self, base: float, exp: float) -> float:
        """Calculate power"""
        return math.pow(base, exp)
    
    def square_root(self, n: float) -> float:
        """Calculate square root"""
        if n < 0:
            raise ValueError("Square root not defined for negative numbers")
        return math.sqrt(n)
    
    def average(self, numbers: List[Union[int, float]]) -> float:
        """Calculate average"""
        return sum(numbers) / len(numbers) if numbers else 0
    
    def median(self, numbers: List[Union[int, float]]) -> float:
        """Calculate median"""
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    
    def standard_deviation(self, numbers: List[Union[int, float]]) -> float:
        """Calculate standard deviation"""
        avg = self.average(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)
    
    def sum_of_squares(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate sum of squares"""
        return sum(x ** 2 for x in numbers)
    
    def is_perfect_square(self, n: int) -> bool:
        """Check if number is perfect square"""
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return root * root == n
    
    def digit_sum(self, n: int) -> int:
        """Calculate sum of digits"""
        return sum(int(d) for d in str(abs(n)))
    
    def demo(self):
        """Demo math utilities"""
        print(f"✓ Factorial of 5: {self.factorial(5)}")
        print(f"✓ Fibonacci (10): {self.fibonacci(10)}")
        print(f"✓ Is 17 prime? {self.is_prime(17)}")
        print(f"✓ GCD(48, 18): {self.gcd(48, 18)}")
        print(f"✓ LCM(12, 18): {self.lcm(12, 18)}")
        print(f"✓ Average [1,2,3,4,5]: {self.average([1,2,3,4,5])}")
        print(f"✓ Median [1,2,3,4,5]: {self.median([1,2,3,4,5])}")
        print(f"✓ Std Dev [1,2,3,4,5]: {self.standard_deviation([1,2,3,4,5]):.2f}")
        print(f"✓ Sum of squares [1,2,3]: {self.sum_of_squares([1,2,3])}")
        print(f"✓ Is 16 perfect square? {self.is_perfect_square(16)}")