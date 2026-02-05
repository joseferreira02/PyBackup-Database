import typer

app = typer.Typer()

@app.command()
def start():
    typer.secho("🚀 Welcome to the Database Backup CLI!", fg=typer.colors.GREEN, bold=True)
    typer.echo("Use `--help` to see available commands like backup and restore.")


if __name__ == "__main__":
    app()