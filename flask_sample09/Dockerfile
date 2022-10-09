FROM python:bullseye

RUN apt update
RUN apt -y upgrade
RUN pip install --upgrade pip
RUN pip install flask
RUN apt install -y vim

WORKDIR /app

COPY ./app /app

CMD [ "python3", "main.py" ]