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


def write_breach(user, breach):
    """Writes a breach to the database

    Args:
        user (str): The user to write the breach for
        breach (dict): The breach data
    """
    with open(USERS_FILE, 'r', encoding='latin-1') as f:
        users = json.load(f)

    if user not in users:
        users[user] = [breach['Name']]
    elif breach['Name'] not in users[user]:
        users[user].append(breach['Name'])

    with open(USERS_FILE, 'w', encoding='latin-1') as f:
        json.dump(users, f, indent=4)

    with open(BREACHES_FILE, 'r', encoding='latin-1') as f:
        data = json.load(f)

    if breach['Name'] not in data:
        data[breach['Name']] = breach

        with open(BREACHES_FILE, 'w', encoding='latin-1') as f:
            json.dump(data, f, indent=4)
