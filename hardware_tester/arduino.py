"""
Arduino module: Handles serial communication with Arduino using HAL.
Enhanced with logging for hardware errors, connection issues, and test results.
"""

from hardware_module import HardwareModule
import random
import logging

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
        try:
            if self.use_mock:
                # MOCK: Simulate Arduino sensor data for testing/demo
                data = {
                    "Boost": round(random.uniform(0, 20), 1),
                    "Oil Pressure": random.randint(0, 80),
                    "Fuel Pressure": random.randint(0, 60),
                    "AFR": round(random.uniform(10, 16), 1),
                    "Water Temp": random.randint(160, 220),
                    "Voltage": round(random.uniform(11, 14), 2),
                    "Current": round(random.uniform(0, 2), 2)
                }
                logging.info(f"Arduino mock data: {data}")
                return data
            # TODO: Implement serial reading from Arduino
            # Simulate error for demonstration
            # raise Exception("Serial connection failed")
            data = {
                "inputs": [],
                "outputs": []
            }
            logging.info(f"Arduino real data: {data}")
            return data
        except Exception as exc:
            logging.error(f"Arduino get_data error: {exc}")
            return {"error": str(exc)}
