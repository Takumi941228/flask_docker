FROM debian:bullseye

RUN apt update
RUN apt -y upgrade
RUN apt -y install nginx
RUN apt install -y vim

COPY default /etc/nginx/sites-available/