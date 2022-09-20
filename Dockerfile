ARG APP_ENV=prod

FROM python:3.10-slim-bullseye AS base

RUN addgroup --system fiuber && adduser --system --group fiuber

WORKDIR /opt/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml ./
RUN apt update && apt install -y curl && \
    curl -sSL https://install.python-poetry.org/ | POETRY_HOME=/opt/poetry python && \
    /opt/poetry/bin/poetry config virtualenvs.create false && \
    /opt/poetry/bin/poetry install --no-root && \
    chown fiuber:fiuber /opt/app

FROM base as prod-preinstall
# RUN echo "copying necesary files for PROD"
COPY src ./src
USER fiuber
CMD python3 -m uvicorn src.main:app --host=0.0.0.0 --port=$PORT

FROM base as dev-preinstall
# RUN echo "Installing necesary libs for DEV"
RUN /opt/poetry/bin/poetry add flake8 coverage pytest
USER fiuber

FROM ${APP_ENV}-preinstall as final

