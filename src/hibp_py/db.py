import json


def get_breaches(account):
    """
    Get all breaches for an account
    :param account: Account to check
    :return: List of breaches
    """
    with open('./data/users.json', 'r') as f:
        data = json.load(f)

    if account in data:
        return data[account]

    return {}


def get_breach(id):
    with open('./data/breaches.json', 'r') as f:
        data = json.load(f)

    if id in data:
        return data[id]

    return {}


def write_breach(user, breach):
    with open('./data/users.json', 'r') as f:
        data = json.load(f)

    if user not in data:
        data[user] = [breach['Name']]

    elif breach['Name'] not in data[user]:
        data[user].append(breach['Name'])

    with open('./data/users.json', 'w') as f:
        json.dump(data, f, indent=4)

    with open('./data/breaches.json', 'r') as f:
        data = json.load(f)

    if breach['Name'] not in data:
        data[breach['Name']] = breach

        with open('./data/breaches.json', 'w') as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    print(get_breaches('mterry@ville.kirkland.qc.ca'))
