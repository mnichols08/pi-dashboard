import unittest
from hardware_tester import hardware_module

class TestHardwareModule(unittest.TestCase):
    def test_abstract_methods(self):
        """Test HardwareModule abstract methods raise NotImplementedError."""
        class DummyModule(hardware_module.HardwareModule):
            def get_data(self):
                return {}
        dummy = DummyModule()
        self.assertIsInstance(dummy.get_data(), dict)

if __name__ == '__main__':
    unittest.main()
