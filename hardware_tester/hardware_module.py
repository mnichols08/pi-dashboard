"""
Base class for hardware modules in the Hardware Abstraction Layer (HAL).
Enhanced with logging for hardware errors and test results.
"""

from abc import ABC, abstractmethod
import logging

class HardwareModule(ABC):
    """
    Abstract base class for hardware modules.
    """
    @abstractmethod
    def get_data(self) -> dict:
        """
        Retrieve data from the hardware module.
        Returns:
            dict: Data from the hardware module.
        """
        try:
            pass
        except Exception as exc:
            logging.error(f"HardwareModule get_data error: {exc}")
            return {"error": str(exc)}
