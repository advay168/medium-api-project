import typer

app = typer.Typer()



@app.command()
def command1():
    typer.echo("Hello World! from command 1")

@app.command()
def command2():
    typer.echo("Hello World! from command 2")

if __name__ == "__main__":
    app()
