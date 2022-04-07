FROM python:3.9.6-alpine

WORKDIR /work

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY ./work /work