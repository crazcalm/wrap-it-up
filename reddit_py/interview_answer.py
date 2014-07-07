__author__ = "crazcalm"

import subreddits, user_class, sort_reddits
from itertools import groupby
from operator import itemgetter

def main():

    # loging in 
    user = user_class.User("crazcalm", "3dKXw24Hv4")
    client = user.login()

    # consuming api
    python_subs = subreddits.list_subreddit_submissions(client, "python", "hot")
    python_subs = [item["data"] for item in python_subs]

    # sorting
    python_subs = sort_reddits.sort_by_key(python_subs, "author")

    # printing out sorted list
    for author, items in groupby(python_subs, key=itemgetter("author")):
        print(author)
        for i in items:
            print("    ", i, "\n")

if __name__ == "__main__":
    main()
