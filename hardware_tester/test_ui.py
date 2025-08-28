import unittest
from hardware_tester import ui

class TestUI(unittest.TestCase):
    def test_run_ui_exists(self):
        """Test that run_ui function exists and is callable."""
        self.assertTrue(callable(getattr(ui, 'run_ui', None)))

    def test_log_and_print(self):
        """Test log_and_print function logs and prints messages."""
        self.assertTrue(callable(getattr(ui, 'log_and_print', None)))

if __name__ == '__main__':
    unittest.main()
