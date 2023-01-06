FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y

RUN mkdir /src
WORKDIR /src
ADD ./src/requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
