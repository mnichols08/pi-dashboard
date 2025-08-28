import unittest
from hardware_tester import ui

class TestUI(unittest.TestCase):
    def test_display(self):
        self.assertTrue(hasattr(ui, 'display'))

    def test_update(self):
        self.assertTrue(hasattr(ui, 'update'))

if __name__ == '__main__':
    unittest.main()
