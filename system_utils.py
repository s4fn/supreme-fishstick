"""System utilities module"""

import os
import platform
import psutil
import socket
import logging

logger = logging.getLogger(__name__)

class SystemUtils:
    """System utilities"""
    
    def get_os_name(self) -> str:
        """Get operating system name"""
        return platform.system()
    
    def get_os_version(self) -> str:
        """Get OS version"""
        return platform.version()
    
    def get_python_version(self) -> str:
        """Get Python version"""
        return platform.python_version()
    
    def get_hostname(self) -> str:
        """Get hostname"""
        return socket.gethostname()
    
    def get_cpu_count(self) -> int:
        """Get CPU count"""
        return os.cpu_count()
    
    def get_cpu_percent(self) -> float:
        """Get CPU usage percentage"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_info(self) -> Dict:
        """Get memory information"""
        mem = psutil.virtual_memory()
        return {
            'total_gb': mem.total / (1024**3),
            'available_gb': mem.available / (1024**3),
            'used_gb': mem.used / (1024**3),
            'percent': mem.percent
        }
    
    def get_disk_info(self, path: str = '/') -> Dict:
        """Get disk information"""
        disk = psutil.disk_usage(path)
        return {
            'total_gb': disk.total / (1024**3),
            'used_gb': disk.used / (1024**3),
            'free_gb': disk.free / (1024**3),
            'percent': disk.percent
        }
    
    def get_process_count(self) -> int:
        """Get process count"""
        return len(psutil.pids())
    
    def get_network_interfaces(self) -> Dict:
        """Get network interface info"""
        return psutil.net_if_addrs()
    
    def is_admin(self) -> bool:
        """Check if running as admin"""
        try:
            return os.getuid() == 0
        except:
            return False
    
    def demo(self):
        """Demo system utilities"""
        print(f"✓ OS: {self.get_os_name()}")
        print(f"✓ Python: {self.get_python_version()}")
        print(f"✓ Hostname: {self.get_hostname()}")
        print(f"✓ CPU Count: {self.get_cpu_count()}")
        print(f"✓ CPU Usage: {self.get_cpu_percent()}%")
        mem = self.get_memory_info()
        print(f"✓ Memory: {mem['used_gb']:.2f}/{mem['total_gb']:.2f}GB")
        disk = self.get_disk_info()
        print(f"✓ Disk: {disk['used_gb']:.2f}/{disk['total_gb']:.2f}GB")
        print(f"✓ Processes: {self.get_process_count()}")