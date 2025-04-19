FROM python:3.12-slim AS builder

RUN pip install poetry
RUN mkdir -p /app
COPY . /app

WORKDIR /app
RUN poetry install --no-root

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "src/main.py"]