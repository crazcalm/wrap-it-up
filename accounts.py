__author__ = 'idclark'
import requests


def user_login(user_name, password, bot_desc):
    """ user_name: a valid reddit username
    password: the respective password to the user name
    bot_desc: the name of the bot to be used in the header dict """

    user_information = {'user': user_name,
                        'passwd': password,
                        'api_type': 'json'}

    headers = {'user-agent': str(bot_desc), }

    client = requests.session()
    client.headers = headers
    response = client.post(r'http://www.reddit.com/api/login', data=user_information)

    if response.json()['json']['errors']:
        error_dict = response.json()['json']['errors']
        raise Exception('Error: '+error_dict[0][0])

    client.user = user_name
    return client

# client is required to get around captcha
def register_account(client, user, pword, rem=True, captcha=None):
    """
    Create a new Reddit account via a valid reddit account. log in with user_login()
    one logged in, you can register new accounts every five minutes without entering captcha.
    """
    user_information = {'user': user,
                        'passwd': pword,
                        'passwd2': pword,
                        'captcha': captcha,
                        'rem': rem,
                        'api_type': 'json'}
    response = client.post(r'http://www.reddit.com/api/register', data=user_information)
    if response.json()['json']['errors']:
        error_dict = response.json()['json']['errors']
        raise Exception('Error: '+error_dict[0][0])
    return response


def delete_account(user, pword, confirm=True):
    """
    LOGIN REQUIRED. input a user and password. confirmation default is True
    """
    data = {'user': user, 'passwd': pword, 'confirm': confirm, 'api_type': 'json'}
    client = user_login(user, pword, 'foo_bar')
    response = client.post(r'http://www.reddit.com/api/delete_user', data=data)
    return response


def current_account_overview(client):
    """
    client: the client created from the user_login() function.
            returns dict (json) of the current user's account overview.
    """
    response = client.get(r'http://www.reddit.com/api/me.json')
    acc_info = response.json()['data']
    if not acc_info:
        raise Exception('No data found, Please user user_login() to log in')
    return acc_info


def user_name_available(name):
    """
    Is the given account name available to create a new account?
    """
    data = {'user': str(name)}
    response = requests.get(r'http://www.reddit.com/api/username_available.json', data=data)
    return response.content




