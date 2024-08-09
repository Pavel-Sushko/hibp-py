import datetime
import json
import time


def load_config(path="config.json"):
    """Load configuration from a JSON file

    Args:
        path (str, optional): Path to the JSON file. Defaults to "config.json".

    Returns:
        dict: Configuration
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def handle_rate_limit(logger):
    """Handle rate limit exceeded"""
    logger.log_event('Rate limit exceeded. Waiting 6 seconds...', 'WARNING')
    time.sleep(6)


class Logger:
    def __init__(self, path="events.log"):
        self.path = path

    def log_event(self, event, severity="INFO"):
        """Log an event to a file

        Args:
            event (str): Event to log
            severity (str, optional): Severity of the event. Defaults to "INFO".
        """
        event_str = f'{datetime.datetime.now()} [{severity}] {event}'

        print(event_str)

        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(event_str + '\n')


if __name__ == "__main__":
    config = load_config()
    print(config)
