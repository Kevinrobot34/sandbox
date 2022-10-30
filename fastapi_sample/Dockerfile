FROM --platform=linux/amd64 python:3.9.10-buster as python-base
ARG DEBIAN_FRONTEND=noninteractive

FROM python-base as initial
RUN apt-get update && apt-get install -y tzdata \
    &&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    &&  apt-get clean \
    &&  rm -rf /var/lib/apt/lists/*

ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org/ | python -
RUN pip install --upgrade pip setuptools

ENV TZ=Asia/Tokyo

FROM initial as app-base
WORKDIR /prototype/
ADD ./pyproject.toml ./poetry.lock /prototype/
ADD src /prototype/src
ADD templates /prototype/templates
RUN poetry install --no-interaction

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]