## BerryGPS-IMU V4 Setup & Testing Guide

This guide covers how to set up and test the BerryGPS-IMU V4 module on your Raspberry Pi for use with the Pi Automotive Dashboard project.

## Hardware Needed
- BerryGPS-IMU V4 module (or compatible)
- Jumper wires

## Wiring
- Connect BerryGPS UART TX/RX to Pi GPIO (pins 14/15)
- Optionally connect I2C (SDA/SCL) for advanced features
- Power via Pi 3.3V or 5V pin

## Troubleshooting
- Ensure GPS antenna is connected
- Check UART/I2C connections
- Use `gpsmon` or `cgps` to verify data

## Usage
- Run `python gps.py` to test GPS data acquisition

### Hardware Setup

1. **Connect BerryGPS-IMU V4 to Raspberry Pi:**
		- Use the provided header pins to connect BerryGPS-IMU to the Pi GPIO.
		- Connect:
				- **I2C:** SDA (GPIO2), SCL (GPIO3), 3.3V, GND
				- **GPS UART:** TX (BerryGPS) → RX (Pi GPIO14), RX (BerryGPS) → TX (Pi GPIO15)
		- Ensure the Pi is powered off during wiring.

2. **Enable Interfaces:**
		- Run `sudo raspi-config` and enable:
				- I2C
				- SPI (if using IMU features)
				- Serial (disable login shell, enable hardware UART)

3. **Verify Connections:**
		- Power on the Pi and run:
				- `i2cdetect -y 1` (should show BerryGPS-IMU at address 0x68)
				- `ls /dev/serial*` (should show serial device for GPS)

### Software Setup

1. **Install Required Packages:**
		- Update and install dependencies:
			```sh
			sudo apt update && sudo apt install -y python3-pip python3-venv python3-dev gpsd gpsd-clients i2c-tools
			```

2. **Configure gpsd:**
		- Edit `/etc/default/gpsd`:
			```sh
			sudo sed -i 's/^DEVICES.*/DEVICES="\/dev\/ttyAMA0"/' /etc/default/gpsd
			sudo systemctl enable --now gpsd
			```

3. **Test GPS Functionality:**
		- Run:
			```sh
			cgps -s
			```
		- You should see live GPS data (lat/lon, speed, satellites).

4. **Test IMU Functionality:**
		- Install Python I2C tools:
			```sh
			pip install smbus2
			```
		- Run a simple test script:
			```python
			import smbus2
			bus = smbus2.SMBus(1)
			address = 0x68
			who_am_i = bus.read_byte_data(address, 0x75)
			print(f"IMU WHO_AM_I: {who_am_i}")
			```
		- Output should match the IMU's expected ID (e.g., 0x68 for MPU9250).

### Troubleshooting

- **No GPS data:**
		- Check UART wiring and gpsd config.
		- Confirm BerryGPS-IMU has a clear view of the sky.
- **No IMU detected:**
		- Check I2C wiring and run `i2cdetect -y 1`.
		- Confirm address 0x68 is present.
- **Permission errors:**
		- Add user to `i2c` and `dialout` groups:
			```sh
			sudo usermod -aG i2c,dialout $USER
			```
		- Reboot Pi.

### References

- [BerryGPS-IMU V4 Documentation](https://ozzmaker.com/berrygps-imu/)
- [gpsd Project](https://gpsd.gitlab.io/gpsd/)

Once setup and tested, BerryGPS-IMU V4 will provide GPS, IMU, and barometric data to your dashboard application.
