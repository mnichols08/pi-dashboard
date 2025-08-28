## DS3231 RTC Setup & Usage Guide for Raspberry Pi

## Overview
This guide explains how to connect, configure, and use the DS3231 Real-Time Clock (RTC) module with your Raspberry Pi for accurate timekeeping, even without internet access.

## Hardware Needed
- DS3231 RTC module
- Jumper wires

## Wiring
- Connect SDA/SCL to Pi GPIO (pins 3/5)
- Power via Pi 3.3V or 5V pin

## Troubleshooting
- Check I2C address (`i2cdetect -y 1`)
- Confirm module is detected
- Replace battery if time resets

## Usage
- Run `python main.py` to sync and read RTC time

### Hardware Required

- Raspberry Pi (any model with I2C support)
- DS3231 RTC module
- Jumper wires

### Wiring the DS3231 to the Pi

1. **Power off your Pi.**
2. **Connect the DS3231 pins:**
	- `VCC` → Pi `3.3V` (Pin 1)
	- `GND` → Pi `GND` (Pin 6)
	- `SDA` → Pi `SDA` (Pin 3, GPIO2)
	- `SCL` → Pi `SCL` (Pin 5, GPIO3)
3. **Double-check connections.**
4. **Power on your Pi.**

### Enable I2C on Raspberry Pi

Run:
```sh
sudo raspi-config
```
Navigate to **Interface Options** → **I2C** → Enable.
Reboot if prompted.

### Install Required Packages

```sh
sudo apt update && sudo apt install -y i2c-tools python3-smbus
```

### Verify DS3231 Connection

Check if the Pi detects the RTC:
```sh
sudo i2cdetect -y 1
```
You should see `0x68` in the output grid (the DS3231 address).

### Set Up the DS3231 as System Clock

1. **Load RTC kernel module:**
	```sh
	sudo modprobe rtc-ds3231
	```
2. **Add to `/boot/config.txt` for auto-load:**
	```sh
	echo 'dtoverlay=i2c-rtc,ds3231' | sudo tee -a /boot/config.txt
	```
3. **Reboot:**
	```sh
	sudo reboot
	```
4. **Check RTC device:**
	```sh
	ls /dev/rtc*
	```

### Set and Read Time from DS3231

1. **Set system time (if needed):**
	```sh
	sudo date -s "2025-08-28 12:00:00"
	```
2. **Write system time to RTC:**
	```sh
	sudo hwclock -w
	```
3. **Read time from RTC:**
	```sh
	sudo hwclock -r
	```

### Use DS3231 in Python

Example using `smbus2`:
```python
import smbus2

bus = smbus2.SMBus(1)
DS3231_ADDR = 0x68
# Read registers, decode BCD, etc. (see datasheet)
```
Or use libraries like `adafruit-circuitpython-ds3231` for easier access.

### Notes

- The Pi will use the DS3231 for timekeeping if no network time is available.
- Replace the coin cell battery on the DS3231 as needed for backup.
- For more advanced usage, see [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/accessories.html#using-an-rtc).

---
This guide helps ensure your Pi dashboard keeps accurate time for logging and timestamping, even when offline.
