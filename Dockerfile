ARG APP_ENV=production

FROM python:3.10-slim-bullseye AS base

RUN addgroup --system fiuber && adduser --system --group fiuber

WORKDIR /opt/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY requirements.txt alembic.ini ./
COPY requirements.txt ./
RUN chown -R fiuber:fiuber /opt/app /tmp && \
    pip install -r requirements.txt

FROM base as production-preinstall
# RUN echo "copying necesary files for PROD"
COPY requirements-prod.txt ./
COPY src ./src
COPY alembic ./alembic
RUN  pip install -r requirements-prod.txt
USER fiuber

CMD bash -c 'sleep 5 && alembic upgrade head && python3 -m uvicorn src.main:app --host=0.0.0.0 --port=$PORT'

FROM base as development-preinstall
# RUN echo "Installing necesary libs for DEV"
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
#USER fiuber
CMD bash

FROM ${APP_ENV}-preinstall as final
