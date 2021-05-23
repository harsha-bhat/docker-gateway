import docker

from .logging import logger


def _parse_labels(labels):
    result = {}
    for label in labels:
        key, value = label.split("=")
        result[key] = value
    return result


def _get_containers():
    client = docker.from_env()
    return client.containers.list()


def _match_labels(container_labels, filter_labels):
    match = True
    for key in filter_labels:
        if key not in container_labels or container_labels[key] != filter_labels[key]:
            match = False
            break
    return match


def _filter_container(containers, filter_labels):
    for container in containers:
        if _match_labels(container.labels, filter_labels):
            return container
    return None


def _container_config(container):
    config = {}
    if container:
        for port_map in container.ports.values():
            for port in port_map:
                config["host"] = port["HostIp"]
                config["port"] = port["HostPort"]
    return config


def get_backend_details(config):
    backends = {}

    containers = _get_containers()

    for backend in config:
        name = backend["name"]
        labels = _parse_labels(backend["match_labels"])
        container = _filter_container(containers, labels)
        backends[name] = _container_config(container)

        if backends[name]:
            logger.info(
                f"Backend {name} - {backends[name]['host']}:{backends[name]['port']}"
            )
        else:
            logger.error(f"Backend not found - {name}")

    return backends
