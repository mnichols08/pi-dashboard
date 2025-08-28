# Pi Automotive Dashboard
A real-time dashboard for any vehicle with compatible sensors—including classics like the 1990 Mitsubishi Eclipse. Contributions and feedback are welcome!

A Raspberry Pi–powered, real‑time automotive dashboard aggregating analog gauges, digital status lights, GPS, and IMU data into a unified UI. Arduino Nano handles 0–5 V analog sensing; the Pi reads digital indicators, GPS, and IMU and renders the dashboard.

## Quick Start

1. **Connect hardware:** Wire your analog sensors (0–5 V) to the Arduino Nano, and digital status lights to the Pi GPIO via a 12 V → 3.3 V divider board. Ensure a common ground.
2. **Flash Arduino:** Upload the provided sketch to your Nano (see `/arduino/`).
3. **Prepare Pi:**
        - Install Raspberry Pi OS Lite or Full.
        - Enable I2C, SPI, and Serial interfaces (`sudo raspi-config`).
        - Install required packages:
            ```sh
            sudo apt update && sudo apt install -y python3-pip python3-venv python3-dev gpsd gpsd-clients i2c-tools
            ```
        - Clone this repo and set up Python environment:
            ```sh
            git clone <this repo>; cd pi-dashboard
            python3 -m venv .venv && source .venv/bin/activate
            pip install -r requirements.txt
            cp config.example.yaml config.yaml
            # Edit config.yaml to match your wiring
            ```
4. **Run the dashboard:**
        ```sh
        source .venv/bin/activate
        python -m app
        ```
5. **View UI:** Open a browser to `http://<pi>:8080` for the dashboard, or connect to the WebSocket stream at `ws://<pi>:8765/stream`.

Works with most vehicles, including the 1990 Mitsubishi Eclipse—just match your sensor wiring and calibration in `config.yaml`.

## Features

- 5 analog automotive gauges via Arduino Nano:
    - Boost, Oil Pressure, Fuel Pressure, AFR, Water Temp (0–5 V)
- Electrical telemetry:
    - System voltage, current (to Arduino analog inputs)
- Digital status lights via custom 12 V → 3.3 V I/O board into Pi GPIO:
    - Cruise, Check Engine, Low Coolant, Oil Pressure, Brake, Seat Belt, Door Ajar, Low Fuel, Charging System Fault, Security
- BerryGPS‑IMU V4 on the Pi:
    - GPS, Accelerometer, Gyroscope, Magnetometer (compass), Barometric/Altitude, Temperature
- Live UI, data logging, calibration, and startup on boot

## High‑Level Architecture

- Arduino Nano
    - Reads analog sensors, averages, timestamps
    - Streams JSON over USB serial (115200) to the Pi
- Raspberry Pi
    - Reads Arduino serial, Pi GPIO (status lights), GPS (gpsd), IMU/baro (I2C/SPI)
    - Fuses data and serves UI + WebSocket stream
    - Persists logs (CSV/Parquet)

```
[Analog Gauges 0–5V] --> Arduino Nano --USB--> Raspberry Pi <--I2C/SPI--> BerryGPS-IMU V4
[Volt/Current 0–5V] -->         |                     ^         ^
                                                                 \---------------------         |
[12V Indicators] -- I/O Board --> Pi GPIO (3.3V)                |
GPS UART --> gpsd ----------------------------------------------
```

## Hardware

- Raspberry Pi (with Wi‑Fi, I2C, SPI, UART enabled)
- Arduino Nano (ATmega328P) or Nano Every
- 5 x 0–5 V analog outputs from gauges: Boost, Oil Pressure, Fuel Pressure, AFR, Water Temp
- Voltage sensor (to 0–5 V), Current sensor (to 0–5 V)
- Custom I/O divider board: 12 V → 3.3 V tolerant digital inputs to Pi GPIO
- BerryGPS‑IMU V4
- Wiring, fusing, and proper grounds (sensor ground and logic ground common)

Notes:
- Pi GPIO is 3.3 V only. Never feed 5 V or 12 V directly to Pi pins.
- Share a single ground between vehicle sensors, Arduino, and Pi.

## Signal Mapping (proposed defaults)

- Arduino Analog (example; edit to match build):
    - A0: Boost
    - A1: Oil Pressure
    - A2: Fuel Pressure
    - A3: AFR
    - A4: Water Temp
    - A5: System Voltage
    - A6: Current Sensor (if available)
- Pi GPIO (example; edit to match board):
    - GPIO5: Check Engine
    - GPIO6: Low Coolant
    - GPIO12: Oil Pressure
    - GPIO13: Brake
    - GPIO16: Seat Belt
    - GPIO17: Door Ajar
    - GPIO18: Low Fuel
    - GPIO19: Charging Fault
    - GPIO20: Security
    - GPIO21: Cruise

Define actual pins in config.

## Data Flow and Protocol

- Arduino → Pi serial (115200, 8N1), JSON Lines (one JSON per line):
```
{"ts": 1730000000, "boost_v": 2.73, "oil_psi_v": 1.20, "fuel_psi_v": 1.00, "afr_v": 3.10, "watert_v": 1.85, "v_batt_v": 4.70, "current_v": 2.10}
```

- Pi enriches with:
    - Lights: {cel, low_coolant, oil, brake, belt, door, low_fuel, charge_fault, security, cruise}
    - GPS: lat, lon, speed, heading, fix, sats, alt
    - IMU: ax, ay, az, gx, gy, gz, mx, my, mz
    - Baro: pressure_hpa, temp_c, altitude_m

- UI subscribes via WebSocket: ws://<pi>:8765/stream

## Calibration and Scaling

Each 0–5 V input maps to engineering units via linear calibration or LUT.

Example config (config.yaml):
```yaml
serial:
    port: /dev/ttyUSB0
    baud: 115200

gpio_inputs:
    cel: 5
    low_coolant: 6
    oil: 12
    brake: 13
    belt: 16
    door: 17
    low_fuel: 18
    charge_fault: 19
    security: 20
    cruise: 21
    invert: []   # add names if active-low

gps:
    use_gpsd: true
    gpsd_host: 127.0.0.1
    gpsd_port: 2947

imu:
    bus: 1
    sample_hz: 50

channels:
    boost:
        source: boost_v
        units: psi
        scale: {m: 20.0, b: -10.0}   # psi = m*volts + b
    oil_pressure:
        source: oil_psi_v
        units: psi
        scale: {m: 50.0, b: 0.0}
    fuel_pressure:
        source: fuel_psi_v
        units: psi
        scale: {m: 50.0, b: 0.0}
    afr:
        source: afr_v
        units: AFR
        scale: {m: 3.0, b: 7.35}     # e.g., Innovate 0–5V -> 7.35–22.39
    water_temp:
        source: watert_v
        units: C
        table:                       # optional LUT for NTC thermistor outputs
            - {v: 0.50, y: 120}
            - {v: 1.00, y: 100}
            - {v: 2.00, y: 80}
            - {v: 3.00, y: 60}
            - {v: 4.00, y: 40}
    v_batt:
        source: v_batt_v
        units: V
        scale: {m: 5.0, b: 0.0}      # adjust for voltage divider ratio
    current:
        source: current_v
        units: A
        scale: {m: 30.0, b: -75.0}   # example for ACS758; set per sensor
logging:
    enabled: true
    path: data/logs
    rotate_mb: 50
ui:
    port: 8080
ws:
    port: 8765
```

## Arduino Firmware (overview)

- Reads analog channels at fixed rate, averages N samples to reduce noise.
- Emits JSON lines with raw volts (0–5 V) for each channel.
- Suggested: 10–50 Hz output rate.

Recommended settings:
- Board: Arduino Nano (Processor: ATmega328P)
- Serial: 115200
- Analog reference: DEFAULT (5 V) or EXTERNAL if using precise ref
- Libraries: none required

Pin note: If using A6/A7 on some Nanos, they are analog‑only.

## Raspberry Pi Setup

1) OS and interfaces
- Raspberry Pi OS Lite (or Full)
- sudo raspi-config → enable:
    - Interface Options: I2C, SPI, Serial (disable login shell, enable hardware UART)
2) Packages
- sudo apt update && sudo apt install -y python3-pip python3-venv python3-dev gpsd gpsd-clients i2c-tools
3) gpsd
- sudo raspi-config set serial to use for hardware, not console
- sudo sed -i 's/^DEVICES.*/DEVICES="\/dev\/ttyAMA0"/' /etc/default/gpsd  # adjust UART if needed
- sudo systemctl enable --now gpsd
4) Project
- git clone <this repo>; cd pi-dashboard
- python3 -m venv .venv && source .venv/bin/activate
- pip install -r requirements.txt  # e.g., pyserial, gpiozero, smbus2, websockets, fastapi, uvicorn, pynmea2, gps3, numpy
- cp config.example.yaml config.yaml and edit

Run:
- source .venv/bin/activate
- python -m app  # starts HTTP UI and WS stream

## Development Notes

- UI: web app renders gauges, indicators, GPS map, plots, and IMU panel.
- Back end:
    - Serial reader: robust JSONL parser with reconnection
    - GPIO: gpiozero with debounce and optional invert
    - GPS: gpsd client for fix/speed/track
    - IMU/Baro: read via smbus2; apply calibration and sensor fusion (e.g., Madgwick)
    - Publisher: WebSocket + optional REST
    - Logger: CSV with headers and ISO timestamps

## Autostart (systemd)

Create /etc/systemd/system/pi-dashboard.service:
```
[Unit]
Description=Pi Automotive Dashboard
After=network-online.target gpsd.service

[Service]
User=pi
WorkingDirectory=/home/pi/pi-dashboard
Environment=PYTHONUNBUFFERED=1
ExecStart=/home/pi/pi-dashboard/.venv/bin/python -m app
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
Enable:

## Safety


## Troubleshooting

- **No serial data from Arduino:**
    - Check USB connection and cable.
    - Confirm Nano is powered and sketch is running.
    - Use `dmesg` or `ls /dev/ttyUSB*` to verify device is detected.
- **Dashboard UI not loading:**
    - Ensure the Python app is running (`python -m app`).
    - Check firewall settings and Pi IP address.
- **Sensors reading incorrectly:**
    - Double-check wiring and grounds.
    - Calibrate channels in `config.yaml`.
    - Verify voltage ranges with a multimeter.
- **Digital status lights not working:**
    - Confirm 12 V → 3.3 V divider board is wired correctly.
    - Check GPIO pin assignments in `config.yaml`.
- **Other issues:**
    - Review logs in `data/logs/`.
    - Consult the README and example configs.
    - Reach out via issues or discussions for help!

## Contributions & Feedback

All users and contributors are welcome! If you have suggestions, bug reports, or improvements, please open an issue or pull request. Feedback from all vehicle types and backgrounds is encouraged.

## Roadmap


 - HVAC integration: Servo motor control for heater temperature, air direction, and flow
 - Clutch and brake pedal switch inputs
 - Gear position sensing using magnetic switches
 - Additional sensor and actuator support as needed

## Repository

Suggested structure:
```
/arduino/               # Arduino sketch
/app/                   # Python backend + UI server
/ui/                    # Web client (optional separate build)
/config.example.yaml
/requirements.txt
/data/logs/
```

## License

MIT (proposed). Edit as needed.

## Credits

Hardware: Arduino Nano, Raspberry Pi, BerryGPS‑IMU V4.