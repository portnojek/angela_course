#nosetests --rednose --cov calculate_python.py
#nosetests --with-coverage calculate_test.py

import unittest
from calculate import Calculate

class TestCalclate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_assert_less(self):
        self.assertLess(1, 2)

if __name__ == '__main__':
    unittest.main()