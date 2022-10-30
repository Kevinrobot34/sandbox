PYTHON_VER      := 3.9.9
VENV_NAME       := fastapi_sample
ARCH            := $(shell uname -m)


virtualenv/create: 
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

virtualenv/install:
	$(eval ret := $(shell pyenv local))
	[ "$(ret)" = "$(VENV_NAME)" ] || (echo '[Error] Virtualenv "$(VENV_NAME)" is NOT activated.' 1>&2 && exit 1)
	poetry install

virtualenv/destroy: 
	pyenv local --unset
	pyenv virtualenv-delete -f $(VENV_NAME)
	pyenv versions

app/run:
	poetry run uvicorn src.main:app --reload

docker/launch:
	docker-compose build
	docker-compose up

docker/rebuild: docker/down
	docker-compose build --no-cache
	docker-compose up

docker/down:
	docker-compose down
