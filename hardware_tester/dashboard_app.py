# dashboard_app.py
# Python GUI Dashboard for Raspberry Pi
# Aggregates data from Arduino, GPS, hardware modules, and voltage divider

import tkinter as tk
from tkinter import ttk
import threading
import time

# Import data source modules
from arduino import ArduinoModule
from gps import GPSModule
from hardware_module import HardwareModule
from voltage_divider import VoltageDividerModule

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi Hardware Dashboard')
        self.geometry('600x400')
        self.create_widgets()
        self.update_interval = 2  # seconds
        self.running = True
        # Instantiate hardware modules
        self.arduino = ArduinoModule(use_mock=True)
        self.gps = GPSModule(use_mock=True)
        self.voltage_divider = VoltageDividerModule(use_mock=True)
        # If you have other hardware modules, instantiate here
        self.start_auto_update()

    def create_widgets(self):
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        self.arduino_frame = ttk.LabelFrame(self, text='Arduino')
        self.arduino_frame.pack(fill='x', padx=10, pady=5)
        self.arduino_label = ttk.Label(self.arduino_frame, text='Loading...')
        self.arduino_label.pack(anchor='w', padx=5, pady=2)

        self.gps_frame = ttk.LabelFrame(self, text='GPS')
        self.gps_frame.pack(fill='x', padx=10, pady=5)
        self.gps_label = ttk.Label(self.gps_frame, text='Loading...')
        self.gps_label.pack(anchor='w', padx=5, pady=2)

    # Removed Hardware Module section

        self.vd_frame = ttk.LabelFrame(self, text='Voltage Divider')
        self.vd_frame.pack(fill='x', padx=10, pady=5)
        self.vd_label = ttk.Label(self.vd_frame, text='Loading...')
        self.vd_label.pack(anchor='w', padx=5, pady=2)

        self.refresh_btn = ttk.Button(self, text='Refresh', command=self.refresh_data)
        self.refresh_btn.pack(pady=10)

    def start_auto_update(self):
        def updater():
            while self.running:
                self.refresh_data()
                time.sleep(self.update_interval)
        threading.Thread(target=updater, daemon=True).start()

    def refresh_data(self):
        # Arduino data
        try:
            arduino_data = self.arduino.get_data()
        except Exception as e:
            arduino_data = f'Error: {e}'
        self.arduino_label.config(text=str(arduino_data))

        # GPS data
        try:
            gps_data = self.gps.get_data()
        except Exception as e:
            gps_data = f'Error: {e}'
        self.gps_label.config(text=str(gps_data))

    # Removed Hardware Module data refresh

        # Voltage Divider data
        try:
            vd_data = self.voltage_divider.get_data()
        except Exception as e:
            vd_data = f'Error: {e}'
        self.vd_label.config(text=str(vd_data))

    def on_close(self):
        self.running = False
        self.destroy()

if __name__ == '__main__':
    app = DashboardApp()
    app.protocol('WM_DELETE_WINDOW', app.on_close)
    app.mainloop()
