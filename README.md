# RGate - Docker Gateway

A configurable command line app to route to docker containers.

### Features

- Built as a [Flask](https://flask.palletsprojects.com/en/2.0.x/) application.
- Runs on a fast, asynchronous WSGI server powered by [bjoern](https://github.com/jonashaag/bjoern).
- Configurable YAML options for routing.
- Get request count and percentile statistics with [TDigest](https://github.com/CamDavidsonPilon/tdigest).

### Prerequisites

RGate requires these dependencies to be installed on the OS.

- Python 3.6+
- Docker
- Docker Compose (only for test containers)
- A C compiler (GCC/Clang)
- libev

To install libev:

##### MacOS

```
brew install libev
```

##### Ubuntu

```
apt-get install libev-dev
```

### Installation

Create a [virtualenv](https://pypi.org/project/virtualenv/) and activate it.

Run this command to install the python dependencies and the rgate CLI.

```
python setup.py install
```

### Usage

Set backend configuration in a config.yml file. Requests from the defined path prefixes are routed to the respective backend containers.

```
routes:
  - path_prefix: /api/payment
    backend: payment
  - path_prefix: /api/orders
    backend: orders

default_response:
  body: "This is not reachable"
  status_code: 403

backends:
  - name: payment
    match_labels:
      - app_name=payment
      - env=production
  - name: orders
    match_labels:
      - app_name=orders
      - env=production

```

Containers are filtered based on the `match_labels` and `default_response` is returned if no containers match.

For testing, you can also use the docker-compose file provided to launch a couple of nginx containers.

```
bash start_services.sh
```

Run the rgate CLI tool with the config file and an optional port:

```
rgate --config config.yml --port 8080
```

### Testing

Run tests with pytest.

```
pytest
```
