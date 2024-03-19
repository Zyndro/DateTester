import unittest
import os
from datetime import datetime
from Tests.Dates_Custom import DateTesterCustom
from Tests.Dates_Predefined import DateTesterPredefined


DateTestsCustom = unittest.TestLoader().loadTestsFromTestCase(DateTesterCustom)
DateTestsPredefined = unittest.TestLoader().loadTestsFromTestCase(DateTesterPredefined)

suite = unittest.TestSuite([DateTestsCustom,DateTestsPredefined])

if __name__ == '__main__':
   log_file = f'{os.path.dirname(os.path.realpath(__file__))}/Reports/RANDOM_DATES_TESTREPORT_{datetime.now().strftime("%d.%m.%Y_%H-%M-%S")}.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f, verbosity=2)
       result = runner.run(suite)