import os
import re
import unittest
import dateutil.parser

__unittest = True
class DateTesterPredefined(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.Months_Short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Oct", "Sep", "Nov", "Dec"]
        self.Months_Long = ["January", "February", "March", "April", "May", "June", "July", "August", "October",
                            "September", "November", "December"]

    @staticmethod
    def loadDates(date):
        data = []
        with open(f'{os.path.dirname(os.path.realpath(__file__))}\..\Dates\{date}') as file:
            for line in file:
                data.append(line.strip(' \n\t'))
        return data

    @staticmethod
    def string_contains_substring(string, substrings):
        for substring in substrings:
            if substring in string:
                return True
        return False

    def test_ISO(self):
        for date in self.loadDates("ISO.txt"):
            ISOdate = re.search(
                '(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+([+-][0-2]\d:[0-5]\d|Z))|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z))|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z))',
                date)
            assert isinstance(ISOdate, re.Match)
            dateutil.parser.parse(date), f"Invalid date '{date}'"


    def test_MM_DD_YYYY(self):
        for date in self.loadDates("MM-DD-YYYY.txt"):
            MMDDYYYYdate = re.search(r'\b^(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[0-1])-(19|20)\d{2}$', date)
            assert isinstance(MMDDYYYYdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date), f"Invalid date '{date}'"

    def test_MM_DD_YYYY_TIME(self):
        for date in self.loadDates("MM-DD-YYYY_Time.txt"):
            MMDDYYYTIMEdate = re.search(r'^(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[0-1])-(19|20)\d{2} (0\d|1\d|2[0-3]):([0-5]\d):([0-5]\d)$', date)
            assert isinstance(MMDDYYYTIMEdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date), f"Invalid date '{date}'"

    def test_MONTH_DATE_YEAR_TIME(self):
        for date in self.loadDates("MONTH DATE YEAR TIME.txt"):
            assert date.startswith(tuple(self.Months_Long)), f"Invalid output '{date}'"
            MMDDYYYTIMEdate = re.search(
                r'^([a-zA-Z\s]*)(0[1-9]|[1-2]\d|3[0-1]) (19|20)\d{2} (0\d|1\d|2[0-3]):([0-5]\d):([0-5]\d)$', date)
            assert isinstance(MMDDYYYTIMEdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date), f"Invalid date '{date}'"

    def test_YEAR_DATE_MONTH_TIME(self):
        for date in self.loadDates("YEAR DATE MONTH TIME.txt"):
            assert self.string_contains_substring(date,self.Months_Long), f"Invalid output '{date}'"
            MMDDYYYTIMEdate = re.search(
                r'^\d{4}-\d{2} .* \d{2}:\d{2}:\d{2}$', date)
            assert isinstance(MMDDYYYTIMEdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date), f"Invalid date '{date}'"

    def test_YYYY_DD_MM_TIME(self):
        for date in self.loadDates("YYYY-DD-MM_Time.txt"):
            MMDDYYYYdate = re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date)
            assert isinstance(MMDDYYYYdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date, dayfirst=True)


    def test_YYYY_MM_DD_TIME(self):
        for date in self.loadDates("YYYY-MM-DD_Time.txt"):
            MMDDYYYYdate = re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date)
            assert isinstance(MMDDYYYYdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date), f"Invalid date '{date}'"

    def test_YEAR_MONTH_DATE_TIME(self):
        for date in self.loadDates("YEAR MONTH DATE TIME.txt"):
            assert self.string_contains_substring(date, self.Months_Long), f"Invalid output '{date}'"
            MMDDYYYYdate = re.search(r'^\d{4}.*\d{2} \d{2}:\d{2}:\d{2}$', date)
            assert isinstance(MMDDYYYYdate, re.Match), f"Invalid output '{date}'"
            dateutil.parser.parse(date), f"Invalid date '{date}'"

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()
