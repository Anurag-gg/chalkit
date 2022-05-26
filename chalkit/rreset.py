import shutil
import typer


def rreset(path):
    typer.secho("Are you sure you want to reset? (y/n)")
    choice = input()
    if choice == "y":
        try:
            shutil.rmtree(path)
            typer.secho("Reset success!!", fg=typer.colors.BRIGHT_GREEN)
        except:
            typer.secho("Error: No configurations found", fg=typer.colors.BRIGHT_RED)
    else:
        typer.secho("Aborting!!!", fg=typer.colors.BRIGHT_GREEN)
