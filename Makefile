clean: clean-build clean-others clean-pyc clean-test

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-others:
	@find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

deps:
	pip3 install -r requirements.txt

free:
	pip3 freeze > requirements.txt

run:
	python3 run.py
