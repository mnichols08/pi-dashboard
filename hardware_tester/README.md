# Hardware Tester

A terminal-based suite for testing Raspberry Pi and Arduino hardware integration.

## Modules

# Hardware Tester Modules

## Module Overview
- `main.py`: Entry point for hardware testing.
- `arduino.py`: Communicates with Arduino devices.
- `gps.py`: Reads and parses GPS data.
- `voltage_divider.py`: Calculates voltage divider readings.
- `ui.py`: Provides a simple user interface for hardware tests.

## Dependencies
Install required Python packages:
```
pip install -r requirements.txt
```

## Example Usage
Run the main tester:
```
python main.py
```

## Module Details
- Each module contains docstrings describing its functions and usage.
- See `testing/` for hardware-specific test instructions.

- Libraries: `pyserial`, `RPi.GPIO` or `gpiozero`, `rich` or `curses`

## Usage
Run `python main.py` from the `hardware_tester` directory.
