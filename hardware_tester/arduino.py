"""
Arduino module: Handles serial communication with Arduino using HAL.
"""

from hardware_module import HardwareModule

import random

class ArduinoModule(HardwareModule):
    """
    Arduino hardware module implementing HardwareModule interface.
    """
    def __init__(self, use_mock: bool = False):
        self.use_mock = use_mock

    def get_data(self) -> dict:
        """
        Retrieve data from Arduino via serial communication or mock for testing.
        Returns:
            dict: Dictionary of Arduino sensor values.
        """
        if self.use_mock:
            # MOCK: Simulate Arduino sensor data for testing/demo
            return {
                "Boost": round(random.uniform(0, 20), 1),
                "Oil Pressure": random.randint(0, 80),
                "Fuel Pressure": random.randint(0, 60),
                "AFR": round(random.uniform(10, 16), 1),
                "Water Temp": random.randint(160, 220),
                "Voltage": round(random.uniform(11, 14), 2),
                "Current": round(random.uniform(0, 2), 2)
            }
        # TODO: Implement serial reading from Arduino
        return {
            "inputs": [],
            "outputs": []
        }
