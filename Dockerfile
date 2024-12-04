FROM geopython/pygeoapi:latest

LABEL maintainer="Carsten Ehbrecht <ehbrecht@dkrz.de>"

# Volume mapping cannot be used with webhook
# https://github.com/maccyber/micro-dockerhub-hook
# simply copy config into Image.
COPY pygeoapi-config.yml /pygeoapi/local.config.yml
# ADD ./data /pygeoapi/data
# Should now be in pygeoapi Docker Image

# COPY ./demo.pygeoapi.io.cron /etc/cron.d/demo.pygeoapi.io.cron

# RUN pip3 install pygeometa
