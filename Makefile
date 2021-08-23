# Don't forget to use tabs (not spaces) on makefile only
# Otherwise, you'll get "*** missing separator."

# Reference only, because not idempotent)
# create_env:
# 	conda env create -f environment.yml
# 	activate pygamer

# Reference only because of risk of wiping out existing env
# remove_env:
#     conda remove --name pygamer --all

# idempotent (just remember to activate the correct env first!)
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Windows only
build_exe:
	pip install pyinstaller
	pyinstaller --onefile --name Snake.exe Main.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	# pass

build_env:
	pip freeze > requirements.txt
	conda env export > environment.yml

all: install format lint test build_env