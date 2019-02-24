from datetime import datetime

class Helper:

    @staticmethod
    def convert_date_to_datetime(date=None):
        """
        converts a date string into a datetime object
        Args:
            date (string): string representing a datetime

        Returns:
            mixed: datetime object, None otherwise
        """
        if not date:
            return None

        try:
            return datetime.strptime(date, '%Y%m%dT%H%M%SZ')
        except ValueError:
            return None
