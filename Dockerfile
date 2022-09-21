ARG APP_ENV=prod

FROM python:3.10-slim-bullseye AS base

RUN addgroup --system fiuber && adduser --system --group fiuber

WORKDIR /opt/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN chown fiuber:fiuber /opt/app && \
    pip install -r requirements.txt

FROM base as prod
# RUN echo "copying necesary files for PROD"
COPY src ./src
USER fiuber
CMD python3 -m uvicorn src.main:app --host=0.0.0.0 --port=$PORT

FROM base as dev
# RUN echo "Installing necesary libs for DEV"
RUN pip install flake8==5.0.4 \
    coverage==6.4.4 \
    pytest==7.1.3
USER fiuber
CMD bash
