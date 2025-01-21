FROM python:3.12-slim

RUN pip install poetry

COPY poetry.lock pyproject.toml README.md /src/
COPY wiki /src/wiki

WORKDIR /src/wiki
RUN poetry install --without dev

ENTRYPOINT ["poetry", "run", "python", "-m", "app"]
