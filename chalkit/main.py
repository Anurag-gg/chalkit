import os
import json
import typer
from appdirs import user_config_dir
from setup import setup
from editor import editor
from rreset import rreset

app = typer.Typer()
config_dir = user_config_dir("chalkit")


@app.command()
def chalkit(reset: bool = False ,view: bool = False):
    if reset:
        rreset(config_dir)
    elif view:
        pass
    else:
        try:
            f = open(os.path.join(config_dir, "config.json"))
            data = json.load(f)
            path = data["path"]
            f.close()
            editor(path)
        except (FileNotFoundError, AttributeError, json.decoder.JSONDecodeError):
            setup(config_dir)
        except Exception as e:
            typer.secho(f"Error:{e}", fg=typer.colors.BRIGHT_RED)


app()
