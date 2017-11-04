FROM resin/rpi-raspbian
ENV READTHEDOCS True
ENV INITSYSTEM on

RUN apt-get update -q &&\
    apt-get install -yq sense-hat python-pip python-picamera libraspberrypi-bin

RUN pip install ISStreamer

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD [ "bash", "start.sh" ]
