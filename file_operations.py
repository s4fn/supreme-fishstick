"""File operations module"""

import os
import shutil
import glob
from pathlib import Path
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class FileOps:
    """File operations utilities"""
    
    def create_file(self, filepath: str, content: str = "") -> bool:
        """Create a new file"""
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w') as f:
                f.write(content)
            logger.info(f"Created file: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to create file: {e}")
            return False
    
    def read_file(self, filepath: str) -> Optional[str]:
        """Read file contents"""
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Failed to read file: {e}")
            return None
    
    def append_to_file(self, filepath: str, content: str) -> bool:
        """Append content to file"""
        try:
            with open(filepath, 'a') as f:
                f.write(content)
            logger.info(f"Appended to file: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to append: {e}")
            return False
    
    def delete_file(self, filepath: str) -> bool:
        """Delete a file"""
        try:
            os.remove(filepath)
            logger.info(f"Deleted file: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete: {e}")
            return False
    
    def copy_file(self, src: str, dst: str) -> bool:
        """Copy a file"""
        try:
            shutil.copy2(src, dst)
            logger.info(f"Copied {src} to {dst}")
            return True
        except Exception as e:
            logger.error(f"Failed to copy: {e}")
            return False
    
    def move_file(self, src: str, dst: str) -> bool:
        """Move a file"""
        try:
            shutil.move(src, dst)
            logger.info(f"Moved {src} to {dst}")
            return True
        except Exception as e:
            logger.error(f"Failed to move: {e}")
            return False
    
    def get_file_size(self, filepath: str) -> Optional[int]:
        """Get file size in bytes"""
        try:
            return os.path.getsize(filepath)
        except Exception as e:
            logger.error(f"Failed to get size: {e}")
            return None
    
    def list_files(self, directory: str, pattern: str = "*") -> List[str]:
        """List files in directory"""
        try:
            return glob.glob(os.path.join(directory, pattern))
        except Exception as e:
            logger.error(f"Failed to list files: {e}")
            return []
    
    def create_directory(self, dirpath: str) -> bool:
        """Create a directory"""
        try:
            Path(dirpath).mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dirpath}")
            return True
        except Exception as e:
            logger.error(f"Failed to create directory: {e}")
            return False
    
    def delete_directory(self, dirpath: str) -> bool:
        """Delete a directory"""
        try:
            shutil.rmtree(dirpath)
            logger.info(f"Deleted directory: {dirpath}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete directory: {e}")
            return False
    
    def file_exists(self, filepath: str) -> bool:
        """Check if file exists"""
        return os.path.exists(filepath)
    
    def get_file_extension(self, filepath: str) -> str:
        """Get file extension"""
        return Path(filepath).suffix
    
    def rename_file(self, old_name: str, new_name: str) -> bool:
        """Rename a file"""
        try:
            os.rename(old_name, new_name)
            logger.info(f"Renamed {old_name} to {new_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to rename: {e}")
            return False
    
    def demo(self):
        """Demo file operations"""
        test_dir = "test_files"
        self.create_directory(test_dir)
        
        test_file = os.path.join(test_dir, "test.txt")
        self.create_file(test_file, "Hello, Big Utility!\n")
        
        content = self.read_file(test_file)
        print(f"✓ Created and read file: {content.strip()}")
        
        self.append_to_file(test_file, "This is appended content.\n")
        print("✓ Appended content to file")
        
        size = self.get_file_size(test_file)
        print(f"✓ File size: {size} bytes")
        
        files = self.list_files(test_dir)
        print(f"✓ Files in directory: {files}")
        
        # Cleanup
        self.delete_directory(test_dir)
        print("✓ Cleanup complete")