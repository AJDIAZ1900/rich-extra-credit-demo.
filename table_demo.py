from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Sample Inventory")

table.add_column("Item", justify="left", style="cyan")
table.add_column("Qty", justify="right", style="green")
table.add_column("Price", justify="right", style="magenta")

table.add_row("USB-C Cable", "12", "$9.99")
table.add_row("SSD 1TB", "4", "$79.00")
table.add_row("HDMI Adapter", "7", "$12.50")

console.print(table)
