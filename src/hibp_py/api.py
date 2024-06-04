import os
import requests
from hibp_py.utils import load_config

config = load_config()

API = {
    'endpoint': 'https://haveibeenpwned.com/api/v3/',
    'headers': {
        'User-Agent': 'hibp-py',
        'hibp-api-key': config['API_KEY']
    }
}


class AuthenticationError(Exception):
    """Raised when authentication fails"""
    pass


class ServerError(Exception):
    """Raised when the server returns an error"""
    pass


class RateLimitError(Exception):
    """Raised when the rate limit is exceeded"""
    pass


def get_breaches(account):
    """
    Get all breaches for an account
    :param account: Account to check
    :return: List of breaches
    """
    response = requests.get(
        f'{API["endpoint"]}breachedaccount/{account}', headers=API['headers'])

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise AuthenticationError('Invalid API key')
    elif response.status_code == 404:
        return {}
    elif response.status_code == 429:
        raise RateLimitError(
            'Rate limit exceeded. Please wait and try again later.')
    else:
        raise ServerError(
            f'Server returned error code: {response.status_code}')


def get_breach(breach_name):
    response = requests.get(
        f'{API["endpoint"]}breach/{breach_name}', headers=API['headers'])

    if response.status_code == 200:
        return response.json()
    else:
        raise ServerError(
            f'Server returned error code: {response.status_code}')
