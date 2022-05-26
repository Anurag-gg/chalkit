# chalkit
Chalkit is a CLI tool to save ideas/todos by just opening your terminal.
The git repository is automatically committed and pushed.

Lets you quickly type your ideas/todos using the terminal and continue on with your work.

![Demo]()

# Initital setup
Requires a directory containing git repository with a README.md file in it.
When you run chalkit for the first time, it asks for the absolute path for this directory.

The configuration files are stored as determined by user_config_dir mentioned by [appdirs](https://pypi.org/project/appdirs/)

# How to install
``` 
$ pip install chalkit
```

# Commands
```
 $ eureka    First time setup, edit ur ideas
```

## Flags
```
$ --view      View your ideas in read-only mode
$ --reset     Reset your configurations
```
# Improvements
Feel free to raise issues, ask for features. Leave a star if helpful.