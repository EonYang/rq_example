install:
	@echo "updating pip"
	@python -m pip install -q --upgrade pip
	@pip install -e .


clean_venv:
	@echo "deleteing current rq-minimal venv"
	@- pyenv virtualenv-delete -f rq-minimal
	@echo "creating new venv rq-minimal"
	@pyenv virtualenv 3.7.6-clean rq-minimal
	@pyenv local rq-minimal
	@echo "using a clean env called rq-minimal"
