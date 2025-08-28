import unittest
from hardware_tester import gps

class TestGPS(unittest.TestCase):
    def test_connect(self):
        self.assertTrue(hasattr(gps, 'connect'))

    def test_get_location(self):
        self.assertTrue(hasattr(gps, 'get_location'))

if __name__ == '__main__':
    unittest.main()
