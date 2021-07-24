FROM python:3.8.3-buster

RUN apt-get update && apt-get install -y git bash
RUN pip install flake8 autopep8 pymysql uwsgi mysqlclient pyyaml
RUN pip install Django==3.0.6

WORKDIR /home/python/app
RUN useradd -u 1000 -om python && \
    chown -R python:python /home/python

ENTRYPOINT [ "/bin/bash","/home/python/app/docker/python/start.sh" ]