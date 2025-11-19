"""Date and time utilities module"""

from datetime import datetime, timedelta, timezone
import time
import logging

logger = logging.getLogger(__name__)

class DateTimeUtils:
    """Date and time utilities"""
    
    def get_current_datetime(self) -> str:
        """Get current date and time"""
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def get_current_utc(self) -> str:
        """Get current UTC time"""
        return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    
    def days_between(self, date1: str, date2: str, fmt: str = '%Y-%m-%d') -> int:
        """Calculate days between two dates"""
        d1 = datetime.strptime(date1, fmt)
        d2 = datetime.strptime(date2, fmt)
        return abs((d2 - d1).days)
    
    def add_days(self, date_str: str, days: int, fmt: str = '%Y-%m-%d') -> str:
        """Add days to a date"""
        date = datetime.strptime(date_str, fmt)
        new_date = date + timedelta(days=days)
        return new_date.strftime(fmt)
    
    def add_hours(self, datetime_str: str, hours: int) -> str:
        """Add hours to datetime"""
        dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        new_dt = dt + timedelta(hours=hours)
        return new_dt.strftime('%Y-%m-%d %H:%M:%S')
    
    def get_day_of_week(self, date_str: str) -> str:
        """Get day of week"""
        date = datetime.strptime(date_str, '%Y-%m-%d')
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[date.weekday()]
    
    def is_leap_year(self, year: int) -> bool:
        """Check if year is leap year"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def get_timestamp(self) -> int:
        """Get current timestamp"""
        return int(time.time())
    
    def timestamp_to_datetime(self, timestamp: int) -> str:
        """Convert timestamp to datetime"""
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    def datetime_to_timestamp(self, datetime_str: str) -> int:
        """Convert datetime to timestamp"""
        dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        return int(dt.timestamp())
    
    def get_week_number(self, date_str: str) -> int:
        """Get week number of year"""
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date.isocalendar()[1]
    
    def get_days_in_month(self, year: int, month: int) -> int:
        """Get number of days in month"""
        if month == 2:
            return 29 if self.is_leap_year(year) else 28
        return 31 if month in [1,3,5,7,8,10,12] else 30
    
    def demo(self):
        """Demo date/time utilities"""
        print(f"✓ Current DateTime: {self.get_current_datetime()}")
        print(f"✓ Current UTC: {self.get_current_utc()}")
        print(f"✓ Days between 2025-01-01 and 2025-12-31: {self.days_between('2025-01-01', '2025-12-31')}")
        print(f"✓ Add 10 days to 2025-01-01: {self.add_days('2025-01-01', 10)}")
        print(f"✓ Day of week (2025-01-01): {self.get_day_of_week('2025-01-01')}")
        print(f"✓ Is 2024 leap year? {self.is_leap_year(2024)}")
        print(f"✓ Current timestamp: {self.get_timestamp()}")
        print(f"✓ Is 2025 leap year? {self.is_leap_year(2025)}")
        print(f"✓ Days in Feb 2024: {self.get_days_in_month(2024, 2)}")
        print(f"✓ Week number of 2025-01-01: {self.get_week_number('2025-01-01')}")