default: routes

setup:
	python3 -m venv .venv
	echo . .venv/bin/activate

req:
	pip install -r requirements.txt

dev:
	pip install -r dev-requirements.txt

format:
	autopep8 -i %

FILES=app.py coord/model.py extensions.py
check:
	pycodestyle ${FILES}
	pyflakes ${FILES}

routes: check
	python app.py exit
	

run: 
	./.venv/bin/python app.py

sw:
	curl -X GET "http://localhost:5000/static/swagger.json" -H "accept: */*"

get:
	curl -s -X GET "http://localhost:5000/coord/one" -H "accept: */*"

list:
	curl -s "http://localhost:5000/coords" -H "accept: */*"

add:
	curl -X POST "http://localhost:5000/coord" -H "accept: */*" -H "Content-Type: application/json" -d "{\"id\":\"one\",\"x\":1,\"y\":1}"
