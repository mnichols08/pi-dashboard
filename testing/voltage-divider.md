
# Voltage Divider Testing Guide

## What is a Voltage Divider?
A voltage divider is a simple circuit using two resistors to scale down a higher voltage to a lower voltage. For Pi GPIO, it lets you safely read signals like 12 V automotive logic by reducing them to 3.3 V or less.

## Hardware Needed
- Resistors (e.g., 10kΩ and 3.3kΩ, or as calculated)
- Breadboard or PCB
- Jumper wires
- Multimeter (for testing)

## Wiring
- Connect resistors in series between 12 V source and Pi GPIO
- Tap output between resistors for 3.3 V signal
- Ensure common ground

## Troubleshooting
- Measure output voltage with multimeter
- Verify resistor values
- Check for loose connections

## Usage
- Use for digital status lights or sensor inputs to Pi

**Basic schematic:**

```
	 Vin ----[ R1 ]----+----[ R2 ]---- GND
										|
								 Vout (to Pi GPIO)
```

Where:
- Vin: Input voltage (e.g., 12 V from car)
- Vout: Output voltage (to Pi GPIO)
- R1, R2: Resistor values

**Formula:**
		Vout = Vin × R2 / (R1 + R2)

**Example:**
To scale 12 V down to 3.3 V:
		- R1 = 6.8 kΩ
		- R2 = 2.2 kΩ
		Vout = 12 × 2.2 / (6.8 + 2.2) ≈ 3.23 V

## Schematic Example

```
12V signal ----[6.8kΩ]----+----[2.2kΩ]---- GND
												 |
											Pi GPIO
```

Add a Schottky diode (cathode to Pi GPIO, anode to GND) and a 3.3 V Zener diode (cathode to Pi GPIO, anode to GND) for protection.

## Troubleshooting Tips

- **Output voltage too high:**
	- Check resistor values and connections.
	- Use higher R1 or lower R2 to reduce Vout.
- **Output voltage negative:**
	- Check ground connections.
	- Add a Schottky diode to clamp negative voltage.
- **No voltage at output:**
	- Confirm input voltage is present.
	- Check for broken wires or cold solder joints.
- **Voltage drops when connected to Pi:**
	- Use lower resistor values (e.g., R1 = 1 kΩ, R2 = 330 Ω) to reduce effect of Pi input impedance.

## Best Practices

- Always test with a multimeter before connecting to Pi.
- Use 1% tolerance resistors for accuracy.
- Keep wires short to reduce noise.
- Label all connections and document your wiring.
- If possible, use a buffer IC (e.g., 74LVC245) for extra protection.

## References

- [Raspberry Pi GPIO Voltage Limits](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio-voltage-levels)
- [Voltage Divider Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-voltage-divider)

---

## Why Test?
Before connecting your voltage divider to the Raspberry Pi GPIO, it's critical to verify that the output voltage is within the safe range (0–3.3 V) and that no negative voltage can reach the Pi. Negative voltage or overvoltage can permanently damage the Pi.

## Step-by-Step Testing Guide

1. **Breadboard First:**
	- Assemble your voltage divider on a breadboard.
	- Double-check resistor values and wiring.

2. **Power Up Carefully:**
	- Use a regulated power supply or the vehicle's 12 V source.
	- Connect the input voltage to the divider, but do **not** connect the output to the Pi yet.

3. **Measure Output Voltage:**
	- Use a multimeter to measure the voltage at the divider output (the point that will connect to the Pi GPIO).
	- Confirm the voltage is between 0 V and 3.3 V for all expected input voltages.

4. **Check for Negative Voltage:**
	- Reverse the input polarity briefly (if possible) to simulate wiring mistakes.
	- Ensure the output never goes negative. If it does, adjust your design (see below).

5. **Test Under Load:**
	- Connect a 10 kΩ resistor from the output to ground to simulate the Pi's input impedance.
	- Re-measure the output voltage to ensure it remains in the safe range.

6. **Final Verification:**
	- Only after confirming safe voltages, connect the output to the Pi GPIO.

## Mitigating Negative Voltage Risk

- **Use a Schottky Diode:**
  - Place a Schottky diode (e.g., 1N5819) between the divider output and ground, with the cathode to the output. This clamps any negative voltage to near zero, protecting the Pi.
- **Add a Zener Diode:**
  - For extra protection, add a 3.3 V Zener diode from the output to ground (cathode to output). This clamps any accidental overvoltage.
- **Double-Check Grounds:**
  - Ensure the Pi, divider, and sensor share a common ground. Floating or mismatched grounds can cause negative voltages.

## Risks and Warnings

- **Negative voltage on Pi GPIO can destroy the chip.** Always test with a multimeter before connecting.
- **Overvoltage (>3.3 V) can also damage the Pi.**
- **Never connect vehicle 12 V directly to Pi pins.**

If in doubt, ask for help or post your design for review before connecting to your Pi.
