"""
GPS module: Handles GPS data parsing and communication using HAL.
"""

from hardware_module import HardwareModule

import random

class GPSModule(HardwareModule):
    """
    GPS hardware module implementing HardwareModule interface.
    """
    def __init__(self, use_mock: bool = False):
        self.use_mock = use_mock

    def get_data(self) -> dict:
        """
        Retrieve GPS data from serial and parse NMEA sentences, or mock for testing.
        Returns:
            dict: Dictionary with keys 'mph', 'gyro', 'compass', 'location'.
        """
        if self.use_mock:
            # MOCK: Simulate GPS data for testing/demo
            return {
                "mph": random.randint(0, 120),
                "gyro": random.choice(["OK", "WARN", "FAIL"]),
                "compass": random.choice(["N", "S", "E", "W"]),
                "location": f"{round(random.uniform(-90,90),4)},{round(random.uniform(-180,180),4)}"
            }
        # TODO: Implement serial reading and NMEA parsing
        return {
            "mph": None,
            "gyro": None,
            "compass": None,
            "location": None
        }
