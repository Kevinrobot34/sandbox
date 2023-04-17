PYTHON_VER      := 3.8.13
VENV_NAME       := snowpark_sample


venv/create:
	$(eval ret := $(shell pyenv versions | grep $(PYTHON_VER)))
	@if [ -n "$(ret)" ]; then \
		echo '$(PYTHON_VER) exists'; \
	else \
		(pyenv install $(PYTHON_VER)); \
	fi
	$(eval ret := $(shell pyenv versions | grep $(VENV_NAME)))
	@if [ -n "$(ret)" ]; then \
		echo '$(VENV_NAME) exists'; \
	else \
		(pyenv virtualenv $(PYTHON_VER) $(VENV_NAME)); \
	fi
	pyenv local $(VENV_NAME)
	pyenv versions
	poetry env info

venv/install:
	poetry install

venv/delete:
	pyenv local --unset
	pyenv virtualenv-delete -f $(VENV_NAME)
	pyenv versions