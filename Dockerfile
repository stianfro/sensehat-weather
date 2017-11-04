FROM resin/rpi-raspbian

RUN apt-get update -q &&\
    apt-get install -yq sense-hat python python-pip

RUN pip install ISStreamer

COPY . /usr/src/app

CMD [ "python", "/usr/src/app/sensehat.py" ]