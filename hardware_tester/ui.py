"""
UI module: Terminal UI logic for hardware testing suite.
"""

def run_ui():
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.table import Table

    console = Console()

    def show_menu():
        console.print("[bold cyan]Hardware Tester Suite[/bold cyan]")
        console.print("[green]Select a test:[/green]")
        console.print("1. GPS Test")
        console.print("2. Arduino Test")
        console.print("3. Voltage Divider Test")
        console.print("4. Exit")

    def show_gps(gps_data):
        table = Table(title="GPS Test Results")
        table.add_column("Metric")
        table.add_column("Value")
        table.add_row("MPH", str(gps_data.get("mph", "N/A")))
        table.add_row("Gyro", str(gps_data.get("gyro", "N/A")))
        table.add_row("Compass", str(gps_data.get("compass", "N/A")))
        table.add_row("Location", str(gps_data.get("location", "N/A")))
        console.print(table)

    def show_arduino(arduino_data):
        table = Table(title="Arduino Test Results")
        table.add_column("Input")
        table.add_column("Status")
        unit_map = {
            "AFR": "Air:Fuel Ratio",
            "Fuel Pressure": "PSI",
            "Oil Pressure": "PSI",
            "Voltage": "V",
            "Current": "A",
            "Water Temp": "°F"
        }
        for inp, val in arduino_data.items():
            if inp == "AFR":
                table.add_row("Air:Fuel Ratio", f"{val}:1")
            elif inp == "Fuel Pressure":
                table.add_row("Fuel Pressure", f"{val} PSI")
            elif inp == "Oil Pressure":
                table.add_row("Oil Pressure", f"{val} PSI")
            elif inp == "Voltage":
                table.add_row("Voltage", f"{val} V")
            elif inp == "Current":
                table.add_row("Current", f"{val} A")
            elif inp == "Water Temp":
                table.add_row("Water Temp", f"{val} °F")
            elif inp == "Boost":
                table.add_row("Boost", f"{val} PSI")
            else:
                table.add_row(inp, str(val))
        console.print(table)


    def show_voltage_divider(divider_data):
        table = Table(title="Voltage Divider Test Results")
        table.add_column("Divider")
        table.add_column("Status")
        for name, status in divider_data.items():
            table.add_row(name, str(status))
        console.print(table)

    # Placeholder mock data for demonstration
    gps_data = {"mph": 55, "gyro": "OK", "compass": "N", "location": "37.7749,-122.4194"}
    arduino_data = {
        "Boost": 14.7,  # psi
        "Oil Pressure": 45,  # psi
        "Fuel Pressure": 38,  # psi
        "AFR": 12.5,  # air:fuel ratio
        "Water Temp": 180,  # deg F
        "Voltage": 12.6,  # V
        "Current": 1.2  # A
    }
    divider_data = {f"Divider {i}": "OK" if i % 2 == 0 else "N/A" for i in range(1, 23)}

    while True:
        show_menu()
        choice = Prompt.ask("Enter choice", choices=["1", "2", "3", "4"], default="4")
        if choice == "1":
            show_gps(gps_data)
        elif choice == "2":
            show_arduino(arduino_data)
        elif choice == "3":
            show_voltage_divider(divider_data)
        elif choice == "4":
            console.print("Exiting...")
            break
        console.print("\n")
