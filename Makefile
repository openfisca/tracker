clean:
	find . -name '*.pyc' -exec rm \{\} \;

test:
	flake8
	pytest
