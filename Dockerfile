FROM python:3.10-slim

WORKDIR /app

RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-root

COPY src src

CMD poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
EXPOSE 8000
