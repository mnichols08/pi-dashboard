import unittest
from hardware_tester import voltage_divider

class TestVoltageDivider(unittest.TestCase):
    def test_calculate_voltage(self):
        self.assertTrue(hasattr(voltage_divider, 'calculate_voltage'))

    def test_get_ratio(self):
        self.assertTrue(hasattr(voltage_divider, 'get_ratio'))

if __name__ == '__main__':
    unittest.main()
