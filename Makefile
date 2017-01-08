# Runs the Flask server in debug mode
server:
	FLASK_APP=main.py FLASK_DEBUG=1 flask run

PYTHON_3_LOCATION=$(shell which python3)
# Installs dependancies and sets up the test command script
installation:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	chmod +rwx test
	echo \#!$(PYTHON_3_LOCATION) > temp
	cat test >> temp
	cat temp > test
	rm temp
