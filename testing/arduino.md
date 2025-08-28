---
# Testing Analog Gauges (0–5 V) and Voltage/Current Sensors

This guide covers how to verify the correct operation of the five analog gauge inputs (Boost, Oil Pressure, Fuel Pressure, AFR, Water Temp) and the voltage/current sensors connected to the Arduino Nano.

## Hardware Needed
- Arduino Nano
- USB cable
- Analog sensors (0–5 V)
- Jumper wires
- Multimeter (for testing)
- (Optional) Simulated sensor outputs or potentiometers

## Wiring
- Connect analog sensors to A0–A6 pins
- Connect Nano to Pi via USB
- Ensure common ground between sensors, Arduino, and Raspberry Pi

## Flashing the Nano
- Upload the dashboard Arduino sketch to the Nano using Arduino IDE

## Troubleshooting
- Check serial port settings on Pi
- Verify sensor voltage range
- Confirm Nano is detected (`lsusb` on Pi)

## Usage
- Run `python main.py` on the Pi to start dashboard and read Nano sensor data

## Equipment Needed

- Multimeter (capable of measuring DC voltage)
- Known voltage source (e.g., adjustable bench power supply or voltage divider circuit)
- Test leads
- (Optional) Simulated sensor outputs or potentiometers

## Steps

### 1. Visual Inspection & Wiring Check

- Ensure all sensor wires are securely connected to the correct Arduino analog pins (A0–A6).
- Confirm a common ground between sensors, Arduino, and Raspberry Pi.

### 2. Power On & Arduino Firmware

- Power up the Arduino Nano and Raspberry Pi.
- Upload the dashboard Arduino sketch to the Nano.
- Open a serial monitor (e.g., Arduino IDE, PuTTY) at 115200 baud to view output.

### 3. Testing Each Gauge Input

For each analog input (A0–A4 for gauges, A5 for voltage, A6 for current):

#### a. Apply a Known Voltage

- Disconnect the sensor wire from the vehicle sensor.
- Connect the analog pin to a known voltage source (start with 0 V, then 2.5 V, then 5 V).
- Use a multimeter to verify the applied voltage.

#### b. Observe Serial Output

- Check the serial output for the corresponding channel (e.g., `boost_v`, `oil_psi_v`).
- The reported value should match the applied voltage within ±0.05 V (allowing for ADC tolerance).

#### c. Repeat for All Channels

- Test each channel individually.
- For water temperature (NTC thermistor), use a resistor or voltage divider to simulate expected voltages.

### 4. Voltage & Current Sensor Testing

#### a. Voltage Sensor (A5)

- Apply a known voltage (e.g., 5 V) to the voltage sensor input.
- Confirm the serial output (`v_batt_v`) matches the applied voltage.

#### b. Current Sensor (A6)

- If using a Hall-effect sensor (e.g., ACS758), simulate a current or apply a test voltage.
- Confirm the serial output (`current_v`) changes accordingly.

### 5. End-to-End Test with Pi

- Start the dashboard Python app (`python -m app`).
- Open the dashboard UI in a browser.
- Confirm the gauge readings update in real time as you change input voltages.

### 6. Troubleshooting

- If readings are incorrect:
	- Check wiring and grounds.
	- Verify sensor calibration in `config.yaml`.
	- Confirm the Arduino sketch is running and serial output is valid.
	- Use a multimeter to verify voltages at the Arduino pin.

---

## Setup Instructions
1. Connect the Arduino Nano to your Raspberry Pi via USB.
2. Ensure analog sensors are wired to A0–A6 pins and a common ground is established.
3. Flash the dashboard sketch to the Nano using Arduino IDE.
4. Install required Python packages: `pip install -r requirements.txt`.

## Running the Test
Run in the `hardware_tester` directory:
```powershell
python main.py
```

## Example Output
```
Arduino detected on /dev/ttyUSB0
Sensor readings: [Boost: 2.1V, Oil: 3.0V, Fuel: 1.8V, AFR: 2.5V, Water: 2.9V]
Test passed: All sensors responding
```

## Troubleshooting Tips
- If the Arduino is not detected, check USB connection and port settings.
- Verify sensor voltage range and wiring.
- Use `lsusb` to confirm Nano is detected.
- Check for permission errors accessing the serial port.

## Tips

- Use potentiometers for easy variable voltage testing.
- Document the voltage-to-unit mapping for each sensor in `config.yaml`.
- For real sensors, compare dashboard readings to known-good mechanical gauges.

---
