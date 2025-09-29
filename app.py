from rich.console import Console
from rich.panel import Panel

console = Console()
console.print(Panel.fit("[bold magenta]Hello from Rich![/bold magenta]\nMake CLI output ✨clean✨ and readable."))
console.print("Status: [green]OK[/green] | Next: [yellow]Table demo[/yellow]")
