"""
UI module: Terminal UI logic for hardware testing suite.
Enhanced with logging for hardware errors, connection issues, and test results.
"""

import logging
logging.basicConfig(
    filename='hardware_tester.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)


def run_ui(config: dict, arduino, gps, voltage_divider) -> None:
    """
    Run the terminal-based UI for the hardware testing suite.
    Presents a menu and displays test results interactively.
    Accepts config dict for UI preferences and hardware settings, and hardware module instances.
    Enhanced with logging for hardware errors, connection issues, and test results.
    """
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.table import Table

    theme = config.get("ui", {}).get("theme", "dark")
    show_logs = config.get("ui", {}).get("show_logs", True)
    language = config.get("ui", {}).get("language", "en")

    # Use default Console; ignore theme string for now
    console = Console()

    def log_and_print(msg, level="info"):
        if level == "error":
            logging.error(msg)
            console.print(f"[bold red]Error:[/bold red] {msg}")
        elif level == "warning":
            logging.warning(msg)
            console.print(f"[yellow]Warning:[/yellow] {msg}")
        else:
            logging.info(msg)
            if show_logs:
                console.print(f"[grey]{msg}[/grey]")

    def show_menu() -> None:
        """Display the main menu options."""
        console.print(f"[bold cyan]Hardware Tester Suite ({language})[/bold cyan]")
        console.print("[green]Select a test:[/green]")
        console.print("1. GPS Test")
        console.print("2. Arduino Test")
        console.print("3. Voltage Divider Test")
        console.print("4. Exit")

    def show_gps(gps_data: dict) -> None:
        """Display GPS test results in a table.
        Args:
            gps_data (dict): Dictionary of GPS metrics.
        """
        try:
            table = Table(title="GPS Test Results")
            table.add_column("Metric")
            table.add_column("Value")
            table.add_row("MPH", str(gps_data.get("mph", "N/A")))
            # ...existing code...
            log_and_print(f"GPS test results: {gps_data}")
            console.print(table)
        except Exception as exc:
            log_and_print(f"GPS test error: {exc}", level="error")
    # ...existing code...
        table.add_row("Gyro", str(gps_data.get("gyro", "N/A")))
        table.add_row("Compass", str(gps_data.get("compass", "N/A")))
        table.add_row("Location", str(gps_data.get("location", "N/A")))
        console.print(table)

    def show_arduino(arduino_data: dict) -> None:
        """Display Arduino test results in a table.
        Args:
            arduino_data (dict): Dictionary of Arduino sensor values.
        """
        try:
            table = Table(title="Arduino Test Results")
            table.add_column("Input")
            table.add_column("Status")
            unit_map = {
                "AFR": "Air:Fuel Ratio",
                "Fuel Pressure": "PSI",
                "Oil Pressure": "PSI",
                "Voltage": "V",
                "Current": "A",
                "Water Temp": "0F"
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
                    table.add_row("Water Temp", f"{val} 0F")
                elif inp == "Boost":
                    table.add_row("Boost", f"{val} PSI")
                else:
                    table.add_row(inp, str(val))
            log_and_print(f"Arduino test results: {arduino_data}")
            console.print(table)
        except Exception as exc:
            log_and_print(f"Arduino test error: {exc}", level="error")

    def show_voltage_divider(divider_data: dict) -> None:
        """Display voltage divider test results in a table.
        Args:
            divider_data (dict): Dictionary of divider statuses.
        """
        try:
            table = Table(title="Voltage Divider Test Results")
            table.add_column("Divider")
            table.add_column("Status")
            for name, status in divider_data.items():
                table.add_row(name, str(status))
            log_and_print(f"Voltage divider test results: {divider_data}")
            console.print(table)
        except Exception as exc:
            log_and_print(f"Voltage divider test error: {exc}", level="error")

    # Placeholder mock data for demonstration
    if show_logs:
        console.print(f"[blue]Loaded config:[/blue] {config}")
    import random
    def generate_gps_data() -> dict:
        """Simulate new GPS data."""
        return {
            "mph": random.randint(0, 120),
            "gyro": random.choice(["OK", "WARN", "FAIL"]),
            "compass": random.choice(["N", "S", "E", "W"]),
            "location": f"{round(random.uniform(-90,90),4)},{round(random.uniform(-180,180),4)}"
        }

    def generate_arduino_data() -> dict:
        """Simulate new Arduino sensor data."""
        return {
            "Boost": round(random.uniform(0, 20), 1),
            "Oil Pressure": random.randint(0, 80),
            "Fuel Pressure": random.randint(0, 60),
            "AFR": round(random.uniform(10, 16), 1),
            "Water Temp": random.randint(160, 220),
            "Voltage": round(random.uniform(11, 14), 2),
            "Current": round(random.uniform(0, 2), 2)
        }

    def generate_divider_data() -> dict:
        """Simulate new voltage divider statuses."""
        return {f"Divider {i}": random.choice(["OK", "N/A", "WARN"]) for i in range(1, 23)}

    gps_data: dict = gps.get_data()
    arduino_data: dict = arduino.get_data()
    divider_data: dict = voltage_divider.get_data()

    last_choice: str = None
    while True:
        show_menu()
        try:
            choice: str = Prompt.ask("Enter choice", choices=["1", "2", "3", "4"], default="4")
        except Exception as e:
            console.print(f"[red]Error reading input: {e}[/red]")
            continue

        last_choice = choice

        def run_test(choice: str) -> None:
            if choice == "1":
                try:
                    gps_data = gps.get_data()
                    show_gps(gps_data)
                    log_and_print("GPS test completed successfully.")
                    console.print("[bold green]GPS test completed successfully.[/bold green]")
                except Exception as e:
                    log_and_print(f"GPS test failed: {e}", level="error")
                    console.print(f"[red]GPS test failed: {e}[/red]")
            elif choice == "2":
                try:
                    arduino_data = arduino.get_data()
                    show_arduino(arduino_data)
                    log_and_print("Arduino test completed successfully.")
                    console.print("[bold green]Arduino test completed successfully.[/bold green]")
                except Exception as e:
                    log_and_print(f"Arduino test failed: {e}", level="error")
                    console.print(f"[red]Arduino test failed: {e}[/red]")
            elif choice == "3":
                try:
                    divider_data = voltage_divider.get_data()
                    show_voltage_divider(divider_data)
                    log_and_print("Voltage divider test completed successfully.")
                    console.print("[bold green]Voltage divider test completed successfully.[/bold green]")
                except Exception as e:
                    log_and_print(f"Voltage divider test failed: {e}", level="error")
                    console.print(f"[red]Voltage divider test failed: {e}[/red]")
                    show_voltage_divider(divider_data)
                    console.print("[bold green]Voltage divider test completed successfully.[/bold green]")
                except Exception as e:
                    console.print(f"[red]Voltage divider test failed: {e}[/red]")
            elif choice == "4":
                console.print("Exiting...")
                exit()
            else:
                console.print("[yellow]Invalid choice. Please select a valid option.[/yellow]")

        run_test(choice)

        # Offer to refresh or return to menu
        refresh: str = Prompt.ask("Press [r] to refresh data, [m] to return to menu, or [q] to quit", choices=["r", "m", "q"], default="m")
        if refresh == "q":
            console.print("Exiting...")
            break
        elif refresh == "r":
            console.print("Refreshing data...")
            gps_data = gps.get_data()
            arduino_data = arduino.get_data()
            divider_data = voltage_divider.get_data()
            run_test(last_choice)
            continue
        elif refresh == "m":
            console.print("Returning to menu...")
            continue
