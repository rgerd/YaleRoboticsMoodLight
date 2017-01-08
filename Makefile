server:
	FLASK_APP=main.py FLASK_DEBUG=1 flask run

installation:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	chmod +rwx test
	python3Location=$(which python3) echo \#!$(python3Location) > temp
	cat test >> temp
	cat temp > test
	rm temp
