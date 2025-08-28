# Hardware Tester Web Dashboard

This dashboard allows you to visually monitor and test hardware data from your Python modules using a web interface.

## Getting Started

### 1. Install Dependencies

Make sure you have Python 3 installed. Install Flask:

```
pip install flask
```

### 2. Start the Flask Server

Navigate to the `hardware_tester` directory and run:

```
python dashboard_server.py
```

The server will start on `http://localhost:5000`.

### 3. Open the Dashboard

Open `dashboard.html` in your web browser. (You may need to serve it via Flask or a simple HTTP server for AJAX to work.)

### 4. View Hardware Status

- Click "Refresh Status" to fetch the latest hardware data from the Python backend.
- The dashboard displays the data returned by the `/api/status` endpoint.

## Customizing Data

- The backend uses `get_status()` from `hardware_module.py` to fetch data. Update this function to return the hardware data you want to visualize.

## Troubleshooting

- If you see an error, check that the Flask server is running and accessible.
- Ensure all Python dependencies are installed.

## File Overview
- `dashboard_server.py`: Flask backend serving hardware data.
- `dashboard.html`: Web dashboard UI.
- `hardware_module.py`: Example Python module for hardware data (customize as needed).

## License
MIT
