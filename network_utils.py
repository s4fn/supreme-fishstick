"""Network utilities module"""

import socket
import requests
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class NetworkUtils:
    """Network utilities"""
    
    def get_local_ip(self) -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def get_public_ip(self) -> Optional[str]:
        """Get public IP address"""
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            return response.text
        except:
            return None
    
    def is_internet_available(self) -> bool:
        """Check if internet is available"""
        try:
            requests.head('https://www.google.com', timeout=3)
            return True
        except:
            return False
    
    def ping_host(self, host: str) -> bool:
        """Ping a host"""
        try:
            socket.gethostbyname(host)
            return True
        except:
            return False
    
    def get_host_ip(self, hostname: str) -> Optional[str]:
        """Get IP from hostname"""
        try:
            return socket.gethostbyname(hostname)
        except:
            return None
    
    def port_open(self, host: str, port: int, timeout: int = 2) -> bool:
        """Check if port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def make_request(self, url: str, method: str = 'GET', **kwargs) -> Optional[Dict]:
        """Make HTTP request"""
        try:
            response = requests.request(method, url, timeout=10, **kwargs)
            return {
                'status_code': response.status_code,
                'content': response.text,
                'headers': dict(response.headers)
            }
        except Exception as e:
            logger.error(f"Request failed: {e}")
            return None
    
    def demo(self):
        """Demo network utilities"""
        print(f"✓ Local IP: {self.get_local_ip()}")
        print(f"✓ Internet Available: {self.is_internet_available()}")
        print(f"✓ Can ping google.com: {self.ping_host('google.com')}")
        print(f"✓ Port 80 open on google.com: {self.port_open('google.com', 80)}")
        if self.is_internet_available():
            print(f"✓ Public IP: {self.get_public_ip()}")