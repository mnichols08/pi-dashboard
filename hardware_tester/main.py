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
import json
import os
import logging
from ui import run_ui
from arduino import ArduinoModule
from gps import GPSModule
from voltage_divider import VoltageDividerModule

logging.basicConfig(
    filename='hardware_tester.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def load_config(config_path: str = None) -> dict:
    """
    Load configuration from config.json.
    """
    try:
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            config = json.load(f)
        logging.info(f"Loaded config from {config_path}")
        return config
    except Exception as exc:
        logging.error(f"Failed to load config: {exc}")
        raise

def main() -> None:
    """
    Main entry point for hardware testing suite.
    Loads config and runs the terminal UI.
    """
    try:
        config = load_config()
        use_mock = config.get("use_mock", True)  # Default to True for safety; set to False for production
        arduino = ArduinoModule(use_mock=use_mock)
        gps = GPSModule(use_mock=use_mock)
        voltage_divider = VoltageDividerModule(use_mock=use_mock)
        logging.info("Hardware modules initialized.")
        run_ui(config, arduino, gps, voltage_divider)
    except Exception as exc:
        logging.critical(f"Fatal error in main: {exc}")
        print(f"Fatal error: {exc}")

if __name__ == "__main__":
    main()
