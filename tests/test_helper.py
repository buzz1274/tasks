from datetime import datetime
from task_warrior.helper import Helper


class TestHelper(object):
    def test_convert_date_to_datetime_returns_none_on_empty_date(self):
        assert Helper().convert_date_to_datetime() is None

    def test_convert_date_to_datetime_returns_none_on_invalid_date_passed(self):
        assert Helper().convert_date_to_datetime('gdgg6515') is None
        assert Helper().convert_date_to_datetime('20190229T231120Z') is None

    def test_convert_date_to_datetime_returns_date_object_when_valid_date_passed(self):
        date = Helper().convert_date_to_datetime('20190129T231120Z')

        assert isinstance(date, datetime)
