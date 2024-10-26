FROM python:3.12-bookworm
EXPOSE 5000
WORKDIR /src

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_PATH=/opt/poetry \
    POETRY_VERSION=1.8.4

ENV PATH="${POETRY_PATH}/bin:$PATH"

RUN pip3 install poetry==${POETRY_VERSION}
COPY ./poetry.lock ./pyproject.toml ./
COPY src /src
RUN poetry install --no-dev

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]