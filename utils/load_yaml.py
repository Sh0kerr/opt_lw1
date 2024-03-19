from yaml import safe_load


def load_yaml(path: str) -> dict:
    with open(path, "r") as f:
        return safe_load(f)
