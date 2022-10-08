FROM python:bullseye

RUN apt update
RUN apt -y upgrade
RUN pip install --upgrade pip
RUN pip install flask

WORKDIR /app

COPY ./app /app