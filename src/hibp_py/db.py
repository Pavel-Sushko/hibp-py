import json


DATA_DIR = './data'
USERS_FILE = f'{DATA_DIR}/users.json'
BREACHES_FILE = f'{DATA_DIR}/breaches.json'


def get_account_breaches(account):
    """Gets all breaches for an account from the database

    Args:
        account (str): The account to check for breaches

    Returns:
        list: A list of breach names
    """
    with open(USERS_FILE, 'r', encoding='latin-1') as f:
        data = json.load(f)

    if account in data:
        return data[account]

    return []


def get_breach(breach_name):
    """Gets a breach from the database

    Args:
        breach_name (str): The breach to get

    Returns:
        dict: The breach data
    """
    with open(BREACHES_FILE, 'r', encoding='latin-1') as f:
        data = json.load(f)

    if breach_name in data:
        return data[breach_name]

    return {}


def write_breach(user, breach):
    """Writes a breach to the database

    Args:
        user (str): The user to write the breach for
        breach (dict): The breach data

    Returns:
        bool: True if the breach is new, False otherwise
    """
    new_breach = False

    with open(USERS_FILE, 'r', encoding='latin-1') as f:
        users = json.load(f)

    if user not in users:
        new_breach = True
        users[user] = [breach['Name']]
    elif breach['Name'] not in users[user]:
        new_breach = True
        users[user].append(breach['Name'])

    with open(USERS_FILE, 'w', encoding='latin-1') as f:
        json.dump(users, f, sort_keys=True)

    with open(BREACHES_FILE, 'r', encoding='latin-1') as f:
        data = json.load(f)

    if breach['Name'] not in data:
        data[breach['Name']] = breach

        with open(BREACHES_FILE, 'w', encoding='latin-1') as f:
            json.dump(data, f, sort_keys=True)

    return new_breach
