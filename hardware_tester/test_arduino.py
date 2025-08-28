import unittest
from hardware_tester import arduino

class TestArduino(unittest.TestCase):
    def test_connect(self):
        """Test Arduino connect method returns expected mock or error."""
        try:
            result = arduino.ArduinoModule(use_mock=True).get_data()
            self.assertIsInstance(result, dict)
            self.assertIn('status', result)
        except Exception as e:
            self.fail(f"Arduino connect raised exception: {e}")

    def test_read_data(self):
        """Test Arduino read_data returns expected mock data."""
        module = arduino.ArduinoModule(use_mock=True)
        data = module.get_data()
        self.assertIsInstance(data, dict)
        self.assertIn('status', data)
        self.assertIn('sensor', data)

if __name__ == '__main__':
    unittest.main()
