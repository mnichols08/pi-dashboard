
# Raspberry Pi Communication Testing Guide

This guide describes how to verify that your Raspberry Pi is efficiently communicating with all hardware components in the Pi Automotive Dashboard project.

## Hardware Needed
- Raspberry Pi (any model with GPIO)
- MicroSD card
- Power supply
- Network connection

## Configuration
- Install Raspberry Pi OS
- Enable I2C, SPI, and Serial (`sudo raspi-config`)
- Install required packages (see README)

## Troubleshooting
- Check power supply stability
- Verify interface enablement
- Use `dmesg` and `lsmod` for hardware status

## Usage
- Run `python main.py` to start dashboard

## 1. Prerequisites

- Raspberry Pi OS installed and configured (I2C, SPI, Serial enabled)
- All hardware connected: Arduino Nano, BerryGPS-IMU V4, custom I/O divider board, sensors
- Python environment set up (`.venv` activated, dependencies installed)
- `config.yaml` edited to match your wiring

## 2. Serial Communication (Arduino Nano)

**Test Steps:**
- Connect Arduino Nano via USB.
- Run:  
	```sh
	dmesg | grep ttyUSB
	ls /dev/ttyUSB*
	```
- Start the dashboard backend:
	```sh
	source .venv/bin/activate
	python -m app
	```
- Check logs for incoming serial data:
	- Look for JSON lines like:
		```
		{"ts": ..., "boost_v": ..., ...}
		```
- If no data, verify Arduino sketch is running and USB cable is functional.

## 3. GPIO Digital Inputs (Status Lights)

**Test Steps:**
- Confirm 12V → 3.3V divider board is wired to Pi GPIO pins.
- Use Python REPL or a simple script:
	```python
	import gpiozero
	from time import sleep

	cel = gpiozero.DigitalInputDevice(5)
	print("Check Engine:", cel.value)
	# Repeat for other pins as defined in config.yaml
	sleep(1)
	```
- Toggle vehicle status lights and confirm GPIO input changes.

## 4. GPS (BerryGPS-IMU V4)

**Test Steps:**
- Ensure `gpsd` is running:
	```sh
	sudo systemctl status gpsd
	```
- Test GPS data:
	```sh
	cgps -s
	```
- Confirm dashboard logs show GPS fields (lat, lon, speed, etc.).

## 5. IMU/Barometer (BerryGPS-IMU V4)

**Test Steps:**
- Use I2C tools to detect device:
	```sh
	sudo i2cdetect -y 1
	```
- Confirm IMU/baro data in dashboard logs (ax, ay, az, gx, gy, gz, mx, my, mz, pressure_hpa, temp_c).

## 6. WebSocket & UI

**Test Steps:**
- Open browser to `http://<pi>:8080` for dashboard UI.
- Connect to WebSocket at `ws://<pi>:8765/stream` using a client (e.g., `websocat` or browser dev tools).
- Confirm live data updates for all channels.

## 7. Logging

**Test Steps:**
- Check `data/logs/` for recent log files.
- Verify logs contain all expected sensor and status data.

## 8. Troubleshooting

- If any component fails, review wiring, config, and logs.
- Use multimeter to verify voltages.
- Check for errors in Python app output.
