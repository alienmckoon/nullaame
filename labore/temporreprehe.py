from rich.console import Console

console = Console()

name = "John Doe"
resp = {"msg": "example is not running"}

console.print(f"{name}. no starting: {resp['msg']}", style="yellow")
