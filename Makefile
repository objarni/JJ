test: .venv/bin/activate
	( . .venv/bin/activate && NOSE_REDNOSE=1 nosetests )

.venv/bin/activate:
	python3 -m venv .venv
	( . .venv/bin/activate && pip install -r requirements.txt )

clean:
	rm -rf .venv
