__author__ = "crazcalm"

from operator import itemgetter
from itertools import groupby

#    python_subs = [item["data"] for item in python_subs]

def format_my_subreddits(response):
    """
    Returns a list of the content (in dictionary form) from the response.
    """
    tempt = []
    for item in response:
        tempt.append(item["data"])
    return tempt

def sort_by_key(items, key):
    """
    For a given list of dictionaries with consistant key namings, sort by the
    given key.

    sort_by_author = sort_by_key(items, "author")
    """
    items.sort(key = itemgetter(key))
    return items
