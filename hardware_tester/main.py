"""
Main entry point for the hardware testing suite.
Handles UI and orchestrates tests for GPS, Arduino, and voltage dividers.
"""


import json
import os
from ui import run_ui
from arduino import ArduinoModule
from gps import GPSModule
from voltage_divider import VoltageDividerModule


def load_config(config_path: str = None) -> dict:
    """
    Load configuration from config.json.
    """
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        return json.load(f)

def main() -> None:
    """
    Main entry point for hardware testing suite.
    Loads config and runs the terminal UI.
    """
    config = load_config()

    # Determine if mock/test data should be used (from config or default)
    use_mock = config.get("use_mock", True)  # Default to True for safety; set to False for production

    # Instantiate hardware modules with use_mock flag
    arduino = ArduinoModule(use_mock=use_mock)
    gps = GPSModule(use_mock=use_mock)
    voltage_divider = VoltageDividerModule(use_mock=use_mock)

    # Pass hardware modules to UI
    run_ui(config, arduino, gps, voltage_divider)

if __name__ == "__main__":
    main()
