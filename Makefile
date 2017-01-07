server:
	FLASK_APP=main.py FLASK_DEBUG=1 flask run

installation:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
