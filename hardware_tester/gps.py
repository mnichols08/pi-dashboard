"""
GPS module: Handles GPS data parsing and communication using HAL.
Enhanced with logging for hardware errors, connection issues, and test results.
"""

from hardware_module import HardwareModule
import random
import logging

"""
GPS module for hardware tester.
Handles GPS data acquisition and parsing.
"""

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
        try:
            if self.use_mock:
                # MOCK: Simulate GPS data for testing/demo
                data = {
                    "mph": random.randint(0, 120),
                    "gyro": random.choice(["OK", "WARN", "FAIL"]),
                    "compass": random.choice(["N", "S", "E", "W"]),
                    "location": f"{round(random.uniform(-90,90),4)},{round(random.uniform(-180,180),4)}"
                }
                logging.info(f"GPS mock data: {data}")
                return data
            # TODO: Implement serial reading and NMEA parsing
            data = {
                "mph": None,
                "gyro": None,
                "compass": None,
                "location": None
            }
            logging.info(f"GPS real data: {data}")
            return data
        except Exception as exc:
            logging.error(f"GPS get_data error: {exc}")
            return {"error": str(exc)}
