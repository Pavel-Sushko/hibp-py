import datetime
import json
import os
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
    def __init__(self, path="events.log", rotation_size=1000):
        self.path = path
        self.rotation_size = rotation_size  # Rotate after this many lines

    def log_event(self, event, severity="INFO"):
        """Log an event to a file

        Args:
            event (str): Event to log
            severity (str, optional): Severity of the event. Defaults to "INFO".
        """
        event_str = f'{datetime.datetime.now()} [{severity}] {event}'
        print(event_str)

        # Check if we need to rotate the log file before opening it
        if self.should_rotate():
            self.rotate()

        # Log the event after rotation (if needed)
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(event_str + '\n')

    def should_rotate(self):
        """Check if the log file needs to be rotated based on the number of lines"""
        if not os.path.exists(self.path):
            return False

        with open(self.path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return len(lines) >= self.rotation_size

    def rotate(self):
        """Rotate the log file"""
        file_path_no_ext = self.path.split('.')[0]

        # Rename the existing log files in reverse order (9 -> 10, 8 -> 9, etc.)
        for i in range(9, -1, -1):
            path = f'{file_path_no_ext}{i > 0 and f".{i}" or ""}.log'

            if os.path.exists(path):
                os.rename(path, f'{file_path_no_ext}.{i + 1}.log')

        # Create a new empty log file after rotation
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write('')


if __name__ == "__main__":
    config = load_config()
    print(config)
