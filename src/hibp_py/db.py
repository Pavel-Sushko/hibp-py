import json


DATA_DIR = './data'
USERS_FILE = f'{DATA_DIR}/users.json'
BREACHES_FILE = f'{DATA_DIR}/breaches.json'


def get_breaches(account):
    """Gets all breaches for an account from the database

    Args:
        account (str): The account to check for breaches

    Returns:
        list: A list of breach names
    """
    with open(USERS_FILE, 'r') as f:
        data = json.load(f)

    if account in data:
        return data[account]

    return []


def get_breach(breach_name):
    """Gets a breach from the database

    Args:
        name (str): The name of the breach

    Returns:
        dict: A dictionary containing the breach data
    """
    with open(BREACHES_FILE, 'r') as f:
        data = json.load(f)

    if id in data:
        return data[breach_name]

    return {}


def write_breach(user, breach):
    """Writes a breach to the database

    Args:
        user (str): The user to write the breach for
        breach (dict): The breach data
    """
    with open(USERS_FILE, 'r') as f:
        data = json.load(f)

    if user not in data:
        data[user] = [breach['Name']]

    elif breach['Name'] not in data[user]:
        data[user].append(breach['Name'])

    with open(USERS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    with open(BREACHES_FILE, 'r') as f:
        data = json.load(f)

    if breach['Name'] not in data:
        data[breach['Name']] = breach

        with open(BREACHES_FILE, 'w') as f:
            json.dump(data, f, indent=4)
