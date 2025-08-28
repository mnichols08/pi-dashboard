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

    def show_gps():
        table = Table(title="GPS Test Results (Placeholder)")
        table.add_column("Metric")
        table.add_column("Value")
        table.add_row("MPH", "N/A")
        table.add_row("Gyro", "N/A")
        table.add_row("Compass", "N/A")
        table.add_row("Location", "N/A")
        console.print(table)

    def show_arduino():
        table = Table(title="Arduino Test Results (Placeholder)")
        table.add_column("Input/Output")
        table.add_column("Value")
        table.add_row("Inputs", "N/A")
        table.add_row("Outputs", "N/A")
        console.print(table)

    def show_voltage_divider():
        table = Table(title="Voltage Divider Test Results (Placeholder)")
        table.add_column("Divider")
        table.add_column("Status")
        table.add_row("Divider 1", "N/A")
        table.add_row("Divider 2", "N/A")
        console.print(table)

    while True:
        show_menu()
        choice = Prompt.ask("Enter choice", choices=["1", "2", "3", "4"], default="4")
        if choice == "1":
            show_gps()
        elif choice == "2":
            show_arduino()
        elif choice == "3":
            show_voltage_divider()
        elif choice == "4":
            console.print("Exiting...")
            break
        console.print("\n")
