FROM resin/raspberrypi3-python:3
ENV READTHEDOCS True
ENV INITSYSTEM on

RUN apt-get update -q &&\
    apt-get install -yq sense-hat python-pip

RUN pip install setuptools picamera ISStreamer

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD [ "bash", "start.sh" ]