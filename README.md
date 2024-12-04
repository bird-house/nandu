# Nandu

**Nandu - the bird**
    This [bird looks like an Emu](https://www.gardenandpatiohomeguide.com/birds-that-look-like-emus/) but its not. The name *Nandu* is mostly used in European countries. Otherwise this bird is called *Rhea*.
    

**Nandu** is an OGC API - Processes implementation using `pygeoapi`. It provides simple processes like a "Say Hello" greeting process.

## Features

- **Hello World Process**: Returns a simple greeting message.
- **Echo Process**: Returns an echo message after some time.

## Quick Guide

Clone the repository:
```console
git clone https://github.com/cehbrecht/nandu.git
cd nandu
```

Create the Conda environment:
```console
conda env create -f environment.yml
conda activate nandu
```

You can use make to run the installation:
```console
make install
```

... and start the service:
```console
make start
```

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

### Install from GitHub

Clone the repository:

```console
git clone https://github.com/cehbrecht/nandu.git
cd nandu
```

Create the Conda environment:

```console
conda env create -f environment.yml
conda activate nandu
```

Install the project dependencies using Poetry:
```console
poetry install
```

## Configuration

Edit pygeoapi config (optional):
```console
vim pygeoapi-config.yml
```

Export paths to configs:

```console
export PYGEOAPI_CONFIG=pygeoapi-config.yml
export PYGEOAPI_OPENAPI=pygeoapi-openapi.yml 
```

Update the OpenAPI configuration:

```console
pygeoapi openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI
```

## Usage

Start the pygeoapi server and expose the processes:
```console
pygeoapi serve
```

This will start the API on http://localhost:5000.


List all processes:

http://localhost:5000/processes



View process details of "Hello World":
http://localhost:5000/processes/hello-world


Execute the process:
```console
curl -X POST http://localhost:5000/processes/hello-world/execution \
     -H "Content-Type: application/json" \
     -d '{
         "inputs": {
             "name": "Alice"
         }
     }'
```

## Development

Run tests:
```console
make test
```

Check coding style:
```console
make lint
```

Build docs:
```console
make docs
```

## Release

Please check the developer guide.

## Examples

See usage examples for the processes in the notebooks folder.

## Docker

You can also use a docker deployment. 

Build images:
```console
docker-compose build
```

Start container:
```console
docker-compose up
```

## License

This project is licensed under the Apache License version 2.


