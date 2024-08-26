from typer import Typer
from TestPolylith.TestComponentA import core

app = Typer(name="TestPolylith")


@app.command()
def test_cli():
    print(core.testFunctionA())
