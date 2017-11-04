FROM resin/rpi-raspbian
ENV READTHEDOCS True

RUN apt-get update -q &&\
    apt-get install -yq sense-hat python python-pip

RUN pip install ISStreamer picamera

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD [ "bash", "start.sh" ]