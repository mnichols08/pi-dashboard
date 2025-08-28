# Hardware Tester

A terminal-based suite for testing Raspberry Pi and Arduino hardware integration.

## Modules
- `main.py`: Entry point, runs the UI and orchestrates tests.
- `gps.py`: GPS data parsing and communication.
- `arduino.py`: Arduino serial communication.
- `voltage_divider.py`: Reads GPIO pins for voltage divider status.
- `ui.py`: Terminal UI logic.

## Setup
- Python 3.x
- Libraries: `pyserial`, `RPi.GPIO` or `gpiozero`, `rich` or `curses`

## Usage
Run `python main.py` from the `hardware_tester` directory.
