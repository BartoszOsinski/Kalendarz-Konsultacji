import click
from app import app


@app.cli.command("mycommand")
def my_command():
    click.echo("Running my custom command!")

# You can add additional commands as needed