import typer

app = typer.Typer()

def handler():
    typer.secho("Please select an option:", fg=typer.colors.YELLOW)
    typer.echo("1) Connect to database")
    typer.echo("2) Exit")
    
    choice = typer.prompt("\nSelect an option")
    
    if choice == "1":
        typer.secho("⚙️  In development\n", fg=typer.colors.CYAN)
        return True  
    elif choice == "2":
        typer.secho("Goodbye! 👋", fg=typer.colors.GREEN)
        return False  
    else:
        typer.secho(f"Invalid option: {choice}. Please select 1 or 2.", fg=typer.colors.RED)
        return True  

@app.command()
def start():
    typer.secho("🚀 Welcome to the Database Backup CLI!", fg=typer.colors.BLUE, bold=True)
    try:
        while True:
            should_continue = handler()
            if not should_continue:
                break
    except Exception as e:
        typer.secho(f"Error: {str(e)}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()