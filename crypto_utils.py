"""Cryptography utilities module"""

import hashlib
import hmac
import base64
from typing import Union
import logging

logger = logging.getLogger(__name__)

class CryptoUtils:
    """Cryptography utilities"""
    
    def md5_hash(self, text: str) -> str:
        """Generate MD5 hash"""
        return hashlib.md5(text.encode()).hexdigest()
    
    def sha1_hash(self, text: str) -> str:
        """Generate SHA1 hash"""
        return hashlib.sha1(text.encode()).hexdigest()
    
    def sha256_hash(self, text: str) -> str:
        """Generate SHA256 hash"""
        return hashlib.sha256(text.encode()).hexdigest()
    
    def sha512_hash(self, text: str) -> str:
        """Generate SHA512 hash"""
        return hashlib.sha512(text.encode()).hexdigest()
    
    def hmac_sha256(self, message: str, key: str) -> str:
        """Generate HMAC SHA256"""
        return hmac.new(
            key.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def base64_encode(self, text: str) -> str:
        """Base64 encode"""
        return base64.b64encode(text.encode()).decode()
    
    def base64_decode(self, text: str) -> str:
        """Base64 decode"""
        try:
            return base64.b64decode(text).decode()
        except:
            return ""
    
    def hash_file(self, filepath: str, algorithm: str = 'sha256') -> str:
        """Hash a file"""
        hash_func = getattr(hashlib, algorithm)()
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except Exception as e:
            logger.error(f"Failed to hash file: {e}")
            return ""
    
    def demo(self):
        """Demo crypto utilities"""
        text = "Hello World"
        print(f"✓ MD5: {self.md5_hash(text)}")
        print(f"✓ SHA256: {self.sha256_hash(text)}")
        print(f"✓ Base64: {self.base64_encode(text)}")
        print(f"✓ HMAC-SHA256: {self.hmac_sha256(text, 'secret')}")