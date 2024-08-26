from typer import Typer
from TestPolylith.TestComponentB import core

app = Typer(name="TestPolylith")


@app.command()
def test_cli():
    print(core.testFunctionA())
