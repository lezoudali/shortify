test:
	python -m pytest

clean:
	rm -rf `find . -name __pycache__`
	rm -rf `find . -name .pytest_cache`

.PHONY: clean
