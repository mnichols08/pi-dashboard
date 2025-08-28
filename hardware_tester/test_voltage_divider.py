import unittest
from hardware_tester import voltage_divider

class TestVoltageDivider(unittest.TestCase):
    def test_get_data_mock(self):
        """Test get_data returns mock data in expected format."""
        module = voltage_divider.VoltageDividerModule(use_mock=True)
        data = module.get_data()
        self.assertIsInstance(data, dict)
        self.assertIn('status', data)
        self.assertIn('voltage', data)

    def test_get_data_real(self):
        """Test get_data with use_mock=False raises NotImplementedError (until GPIO is implemented)."""
        module = voltage_divider.VoltageDividerModule(use_mock=False)
        try:
            module.get_data()
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
        else:
            self.fail("Expected NotImplementedError for real hardware access.")

if __name__ == '__main__':
    unittest.main()
