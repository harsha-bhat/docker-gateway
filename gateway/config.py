import yaml


def load_config(path):
    """Parse YAML config file"""
    with open(path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config
