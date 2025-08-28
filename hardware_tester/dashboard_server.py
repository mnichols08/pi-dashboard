
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from hardware_module import HardwareModule
import os
import voltage_divider
import arduino
import gps


app = Flask(__name__, static_folder=None)
CORS(app)  # Enable CORS for development


# API: Hardware status
@app.route('/api/status')
def get_status():
    try:
        voltage = voltage_divider.get_voltage_data()
        arduino_data = arduino.ArduinoModule(use_mock=True).get_data()
        gps_data = gps.GPSModule(use_mock=True).get_data()
        rtc_data = {'datetime': '2025-08-28 12:34:56'}  # Placeholder, replace with real RTC module if available
        return {
            'voltage_divider': voltage,
            'arduino': arduino_data,
            'gps': gps_data,
            'rtc': rtc_data
        }
    except Exception as e:
        return {'error': str(e)}

@app.route('/api/status')
def status():
    data = get_status()
    return jsonify(data)

# API: Voltage divider data
@app.route('/api/voltage')
def voltage():
    try:
        vdata = voltage_divider.get_voltage_data()  # You may need to implement this
    except Exception as e:
        vdata = {'error': str(e)}
    return jsonify(vdata)

# API: Hardware logs (example)
@app.route('/api/logs')
def logs():
    log_path = os.path.join(os.path.dirname(__file__), '../hardware_tester.log')
    try:
        with open(log_path, 'r') as f:
            lines = f.readlines()[-50:]  # Last 50 lines
        return jsonify({'logs': lines})
    except Exception as e:
        return jsonify({'error': str(e)})

# Serve dashboard.html via Flask
@app.route('/')
def dashboard():
    return send_from_directory(os.path.dirname(__file__), 'dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
