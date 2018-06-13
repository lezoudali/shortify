test:
	python -m pytest

clean:
	rm -rf `find . -name __pycache__`
	rm -rf `find . -name .pytest_cache`

dev:
	FLASK_ENV=development FLASK_APP=shortify.app.py:application flask run

.PHONY: clean test
