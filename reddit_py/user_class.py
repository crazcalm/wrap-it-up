import accounts, users, subreddits
import getpass

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return accounts.user_login(self.username, self.password)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Username: %s" % self.username

def initialize_user():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    user = User(username, password)
    return user

if __name__ == "__main__":
    user = initialize_user()
    print(user)
