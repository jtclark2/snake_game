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

Windows:
    A .exe is checked in (should be up-to-date, though I'm manually maintaining it,
    since it needs to build in Windows, and build server is linux)
    If you want to rebuild, using the following commands output to `dist\Snake.exe`

    ```	
    pip install pyinstaller
	pyinstaller --onefile --name Snake.exe Main.py
	```

# Future Improvements

## Medium Priority
- Unit Testing

## Low Priority:
- Fix Pause UX for .exe build
- Fix apple spawning (so that apples never spawn behind a snake)
- Make "X" close the window