import unittest
from hardware_tester import gps

class TestGPS(unittest.TestCase):
    def test_get_data_mock(self):
        """Test GPSModule get_data returns mock data in expected format."""
        module = gps.GPSModule(use_mock=True)
        data = module.get_data()
        self.assertIsInstance(data, dict)
        self.assertIn('status', data)
        self.assertIn('location', data)

if __name__ == '__main__':
    unittest.main()
