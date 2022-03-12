formatter:
	@black .
	@isort --recursive .
	@flake8

testing:
	@pytest