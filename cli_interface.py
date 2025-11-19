"""CLI interface module"""

import sys
import logging

logger = logging.getLogger(__name__)

class CLIInterface:
    """Command-line interface"""
    
    def __init__(self, utility):
        self.utility = utility
        self.commands = {
            'help': self.show_help,
            'exit': self.exit_program,
            'demo': self.run_demo,
            'file': self.file_menu,
            'string': self.string_menu,
            'math': self.math_menu,
            'time': self.time_menu,
            'system': self.system_menu,
            'network': self.network_menu,
        }
    
    def run(self):
        """Run CLI"""
        print("\n" + "="*60)
        print("BIG PYTHON UTILITY - INTERACTIVE CLI")
        print("="*60)
        print("Type 'help' for available commands\n")
        
        while True:
            try:
                cmd = input(">>> ").strip().lower()
                if cmd in self.commands:
                    self.commands[cmd]()
                elif cmd:
                    print("Unknown command. Type 'help' for available commands.")
            except KeyboardInterrupt:
                self.exit_program()
            except Exception as e:
                logger.error(f"Error: {e}")
    
    def show_help(self):
        """Show help"""
        print("\nAvailable Commands:")
        print("  help      - Show this help message")
        print("  demo      - Run feature demonstration")
        print("  file      - File operations menu")
        print("  string    - String utilities menu")
        print("  math      - Math utilities menu")
        print("  time      - Date/time utilities menu")
        print("  system    - System utilities menu")
        print("  network   - Network utilities menu")
        print("  exit      - Exit program\n")
    
    def run_demo(self):
        """Run demo"""
        self.utility.demo_all_features()
    
    def file_menu(self):
        """File operations menu"""
        filepath = input("Enter file path: ").strip()
        if self.utility.file_ops.file_exists(filepath):
            content = self.utility.file_ops.read_file(filepath)
            print(f"Content: {content}")
        else:
            print(f"File not found: {filepath}")
    
    def string_menu(self):
        """String utilities menu"""
        text = input("Enter text: ").strip()
        print(f"Reversed: {self.utility.string_utils.reverse_string(text)}")
        print(f"Uppercase: {text.upper()}")
        print(f"Lowercase: {text.lower()}")
    
    def math_menu(self):
        """Math utilities menu"""
        try:
            num = int(input("Enter a number: "))
            print(f"Factorial: {self.utility.math_utils.factorial(num)}")
            print(f"Is Prime: {self.utility.math_utils.is_prime(num)}")
        except ValueError:
            print("Invalid number")
    
    def time_menu(self):
        """Date/time utilities menu"""
        print(f"Current Time: {self.utility.date_time_utils.get_current_datetime()}")
        print(f"Current UTC: {self.utility.date_time_utils.get_current_utc()}")
    
    def system_menu(self):
        """System utilities menu"""
        print(f"OS: {self.utility.system_utils.get_os_name()}")
        print(f"Python: {self.utility.system_utils.get_python_version()}")
        mem = self.utility.system_utils.get_memory_info()
        print(f"Memory: {mem['used_gb']:.2f}/{mem['total_gb']:.2f}GB")
    
    def network_menu(self):
        """Network utilities menu"""
        print(f"Local IP: {self.utility.network_utils.get_local_ip()}")
        print(f"Internet: {self.utility.network_utils.is_internet_available()}")
    
    def exit_program(self):
        """Exit program"""
        print("\nGoodbye! 👋")
        sys.exit(0)