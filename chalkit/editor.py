import os
import subprocess
import platform
import typer
import sys
from chalkit.git_commit import git_commit


def editor(path, view_only):
    rpath = os.path.join(path, "README.md")
    gpath = os.path.join(path, ".git")

    if not os.path.isfile(rpath):
        typer.secho(f"Error:File not found at {rpath}", fg=typer.colors.BRIGHT_RED)
        sys.exit()

    if not os.path.isdir(gpath):
        typer.secho(f"Error:Git not found at {gpath}", fg=typer.colors.BRIGHT_RED)
        sys.exit()

    if not view_only:
        typer.secho(
            "Enter the commit message\n> ", fg=typer.colors.BRIGHT_GREEN, nl=False
        )
        commit_message = input()
        if platform.system() == "Windows":
            nano_path = r"C:\Program Files\Git\usr\bin\nano.exe"
            if not os.path.isfile(nano_path):
                typer.secho(
                    f"Make sure nano is installed on correct path:{nano_path}",
                    fg=typer.colors.BRIGHT_RED,
                )
                sys.exit()
            subprocess.call((nano_path, rpath))
        else:
            subprocess.call(("nano", rpath))

        result = git_commit(commit_message, path)
        if result:
            typer.secho(f"Error: {result}", fg=typer.colors.BRIGHT_RED)

    else:
        if platform.system() == "Windows":
            nano_path = r"C:\Program Files\Git\usr\bin\nano.exe"
            if not os.path.isfile(nano_path):
                typer.secho(
                    f"Make sure nano is installed on correct path:{nano_path}",
                    fg=typer.colors.BRIGHT_RED,
                )
                sys.exit()
            subprocess.call((nano_path, "-v", rpath))
        else:
            subprocess.call(("nano", "-v", rpath))
