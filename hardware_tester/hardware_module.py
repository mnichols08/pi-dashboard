"""
Base class for hardware modules in the Hardware Abstraction Layer (HAL).
"""

from abc import ABC, abstractmethod

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
        pass
