import unittest
from unit.app.calculate import Calculate

class TestCalclate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_assert_less(self):
        self.assertLess(1, 2)

if __name__ == '__main__':
    unittest.main()