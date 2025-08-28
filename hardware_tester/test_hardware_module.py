import unittest
from hardware_tester import hardware_module

class TestHardwareModule(unittest.TestCase):
    def test_init(self):
        self.assertTrue(hasattr(hardware_module, '__init__'))

    def test_status(self):
        self.assertTrue(hasattr(hardware_module, 'status'))

if __name__ == '__main__':
    unittest.main()
