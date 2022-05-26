import typer
import os
import json


def welcome():
    typer.secho(
        r"""
#################################################################################
			     _____  
			   .'     `.            WELCOME TO FIRST
			  /         \            TIME SETUP
			 |           | 
			 '.  +^^^+  .'
			   `. \./ .'
			     |_|_|  
			     (___)    
			     (___)
			     `---'
##################################################################################
    """,
        fg=typer.colors.BRIGHT_YELLOW,
    )


def setup(config_dir):
    os.system("cls" if os.name == "nt" else "clear")
    welcome()
    while True:
        typer.secho(
            "Enter the absolute path of your git repo with the README file to save your ideas\n> ",
            fg=typer.colors.BRIGHT_GREEN,
            nl=False,
        )
        choice = input()

        # Check if valid path
        if not os.path.isdir(choice):
            typer.secho("Enter valid absolute path\n", fg=typer.colors.BRIGHT_RED)
            continue

        if not os.path.isdir(os.path.join(choice, ".git")):
            typer.secho(
                "Directory not initialized with git\n", fg=typer.colors.BRIGHT_RED
            )
            continue

        if not os.path.isfile(os.path.join(choice, "README.md")):
            typer.secho("Add a README.md to the repo\n", fg=typer.colors.BRIGHT_RED)
            continue

        # create config files
        if not os.path.isdir(config_dir):
            os.makedirs(config_dir)

        with open(os.path.join(config_dir, "config.json"), "w") as f:
            data = {"path": choice}
            f.write(json.dumps(data))

        typer.secho(
            "\nSuccessfully saved the changes!!\nRun the program again to start writing your ideas",
            fg=typer.colors.GREEN,
        )
        break
