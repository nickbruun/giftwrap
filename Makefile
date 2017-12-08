SOURCE_FILES := giftwrap setup.py
FLAKE8_BIN := pipenv run flake8
PYTHON_BIN := pipenv run python

all:

check:
	@$(FLAKE8_BIN) $(SOURCE_FILES)

publish:
	@python setup.py sdist upload

.PHONY: all check publish
