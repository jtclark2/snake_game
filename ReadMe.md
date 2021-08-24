# SnakeGame
This is the classic game: Snake
A snake runs around a grid world, eating apples, and growing longer. Looping over the edge of the screen is allowed.

# Controls
Arrow Keys control movement.

`p` to pause(the .exe version does not print "Game paused" )

`ENTER` to restart the game

`END` or `X` in the window to close game

# Dependencies
See requirements.txt

# Setup
1) Create an environment (use virtualenv or conda)
    - Build from environment.yml
    `conda env create -f environment.yml` 
    - Build from virtualenv:
    `python3 -m venv ~/.[repoName]`

2) Install dependencies (make sure to enter env first)
    - Build with pip: `pip install -r requirements.txt`

3) Run: `python Main.py`

# Windows .exe:
    To build the .exe, use the following commands (output defaults to `dist\Snake.exe`):

    pip install pyinstaller
	pyinstaller --onefile --name Snake.exe Main.py


# Makefile
Use `make all` prior to commit. (With WSL, you can install on Windows)

# Future Improvements (low priority)
- Unit Testing 
- Fix Pause UX for .exe build (font file isn't being added to .exe correctly, so text is not showing)
- Fix apple spawning (so that apples never spawn behind a snake)