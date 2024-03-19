import os
import re
import unittest


class DateTesterCustom(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.Months_Short = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Oct","Sep","Nov","Dec"]
        self.Months_Long = ["January", "February", "March", "April", "May", "June", "July", "August", "October", "September", "November", "December"]

    @staticmethod
    def loadDates(date):
        data = []
        with open(f'{os.path.dirname(os.path.realpath(__file__))}\..\Dates\{date}') as file:
            for line in file:
                data.append(line.strip(' \n\t'))
        return data


    def test_D_Custom(self):
        for date in self.loadDates("D CUSTOM.txt"):
            Ddate = re.search(r'\b(1?[1-9]|[12][0-9]|3[01])\b', date)
            assert isinstance(Ddate, re.Match), f"Invalid output '{date}'"

    def test_DD_Custom(self):
        for date in self.loadDates("DD CUSTOM.txt"):
            DDdate = re.search(r'\b(0?[1-9]|[12][0-9]|3[01])\b', date)
            assert isinstance(DDdate, re.Match), f"Invalid output '{date}'"

    def test_H_Custom(self):
        for date in self.loadDates("H CUSTOM.txt"):
            Hdate = re.search(r'^((?:[0-9]|1[0-9]|2[0-3])(?:\\d{1,2})?|23)$', date)
            assert isinstance(Hdate, re.Match), f"Invalid output '{date}'"

    def test_HH_Custom(self):
        for date in self.loadDates("HH CUSTOM.txt"):
            HHdate = re.search(r'^(0\d|1\d|2[0-3])$', date)
            assert isinstance(HHdate, re.Match), f"Invalid output '{date}'"

    def test_m_Custom(self):
        for date in self.loadDates("m_CUSTOM.txt"):
            mdate = re.search(r'^([0-9]|[1-5]\d)$', date)
            assert isinstance(mdate, re.Match), f"Invalid output '{date}'"

    def test_MM_Custom(self):
        for date in self.loadDates("MM CUSTOM.txt"):
            MMdate = re.search(r'^(0[1-9]|1[0-2])$', date)
            assert isinstance(MMdate, re.Match), f"Invalid output '{date}'"

    def test_mm_Custom(self):
        for date in self.loadDates("mm_CUSTOM.txt"):
            mmdate = re.search(r'^([0-5]?\d)$', date)
            assert isinstance(mmdate, re.Match), f"Invalid output '{date}'"

    def test_MON_Custom(self):
        for date in self.loadDates("MON CUSTOM.txt"):
            assert date.strip(' \n\t') in self.Months_Short, f"Invalid output '{date}'"

    def test_MONTH_Custom(self):
        for date in self.loadDates("MONTH CUSTOM.txt"):
            assert date.strip(' \n\t') in self.Months_Long, f"Invalid output '{date}'"

    def test_s_Custom(self):
        for date in self.loadDates("s_CUSTOM.txt"):
            sdate = re.search(r'^([0-9]|[1-5]\d)$', date)
            assert isinstance(sdate, re.Match), f"Invalid output '{date}'"

    def test_ss_Custom(self):
        for date in self.loadDates("ss_CUSTOM.txt"):
            ssdate = re.search(r'^([0-5]?\d)$', date)
            assert isinstance(ssdate, re.Match), f"Invalid output '{date}'"

    def test_YY_Custom(self):
        for date in self.loadDates("YY CUSTOM.txt"):
            YYdate = re.search(r'^(0\d|1\d|2\d|3\d|4\d|5\d|6\d|7\d|8\d|9\d)$', date)
            assert isinstance(YYdate, re.Match), f"Invalid output '{date}'"

    def test_YYYY_Custom(self):
        for date in self.loadDates("YYYY CUSTOM.txt"):
            YYdate = re.search(r'^(19\d\d|20\d\d|2100)$', date)
            assert isinstance(YYdate, re.Match), f"Invalid output '{date}'"


    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()
