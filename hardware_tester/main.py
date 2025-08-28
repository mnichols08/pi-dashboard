"""
Main entry point for the hardware testing suite.
Handles UI and orchestrates tests for GPS, Arduino, and voltage dividers.
"""


import json
import os
from ui import run_ui


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
    run_ui(config)

if __name__ == "__main__":
    main()
