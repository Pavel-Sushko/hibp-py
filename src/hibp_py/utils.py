import json


def load_config(path="config.json"):
    """Load configuration from a JSON file

    Args:
        path (str, optional): Path to the JSON file. Defaults to "config.json".

    Returns:
        dict: Configuration
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    config = load_config()
    print(config)
