FROM python:3.9.6-alpine

WORKDIR /work

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 for postgresql
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

# Install requirements
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# Copy project
COPY ./work /work

# Entrypoint
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]