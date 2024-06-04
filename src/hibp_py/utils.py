import json


def load_config(path="config.json"):
    """Load configuration from a JSON file

    Args:
        path (str, optional): Path to the JSON file. Defaults to "config.json".

    Returns:
        dict: Configuration
    """
    with open(path, 'r') as f:
        return json.load(f)


def log_error(error):
    """Log an error

    Args:
        error (str): Error message
    """
    with open("data/error.log", "a") as f:
        f.write(error + "\n")


if __name__ == "__main__":
    config = load_config()
    print(config)
