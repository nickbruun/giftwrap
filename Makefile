SOURCE_FILES := giftwrap setup.py


all:

check:
	@pyflakes $(SOURCE_FILES)
	@pep8 $(SOURCE_FILES)

publish:
	@python setup.py sdist upload

.PHONY: all check publish
