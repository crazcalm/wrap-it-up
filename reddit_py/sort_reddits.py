__author__ = "crazcalm"

from operator import itemgetter
from itertools import groupby

def sort_by_key(items, key):
    """
    For a given list of dictionaries with consistant key namings, sort by the
    given key.

    sort_by_author = sort_by_key(items, "author")
    """
    items.sort(key = itemgetter(key))
    return items
