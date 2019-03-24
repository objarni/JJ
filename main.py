#!/usr/bin/env python3
import os
import sys
import json

from jj import startup_behaviour, Action, HELP_TEXT
from search import search_for
from tomd import result2md


def load_journal(journal_path):
    with open(journal_path) as f:
        return json.loads(f.read())


if __name__ == '__main__':
    args = sys.argv[1:]
    journal_path = os.environ.get('JOURNAL', None)
    result = startup_behaviour(args, journal_path)
    if result == Action.EDIT:
        print("EDIT")
    elif result == Action.SEARCH:
        keyword = sys.argv[1]
        journal = load_journal(journal_path)
        result = search_for(keyword, journal)
        md = result2md(result, keyword)
        print(md)
    else:
        print(result)
