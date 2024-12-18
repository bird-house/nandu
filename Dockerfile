FROM geopython/pygeoapi:latest

LABEL maintainer="Carsten Ehbrecht <ehbrecht@dkrz.de>"
LABEL Description="nandu pygeoapi" Vendor="Birdhouse" Version="0.1.0"

# Volume mapping cannot be used with webhook
# https://github.com/maccyber/micro-dockerhub-hook
# simply copy config into Image.
COPY pygeoapi-config.yml /pygeoapi/local.config.yml
# ADD ./data /pygeoapi/data
# Should now be in pygeoapi Docker Image

# COPY ./demo.pygeoapi.io.cron /etc/cron.d/demo.pygeoapi.io.cron

# Set the working directory to /code
WORKDIR /code

# Copy source code
COPY . /code

# Install
RUN python3 -m pip install --no-cache-dir -e . 