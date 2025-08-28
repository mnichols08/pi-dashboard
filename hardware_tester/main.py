"""
Main entry point for the hardware testing suite.
Handles UI and orchestrates tests for GPS, Arduino, and voltage dividers.
"""

from ui import run_ui

def main() -> None:
    """
    Main entry point for hardware testing suite.
    Runs the terminal UI.
    """
    run_ui()

if __name__ == "__main__":
    main()
