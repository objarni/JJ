#!/usr/bin/env python3
import os
import sys
import json
import webbrowser

from jj import startup_behaviour, Action, HELP_TEXT
from search import search_for
from tomd import result2md
from mdformat import render_html


HTML_TMP_FILE = '/tmp/search_result.html'


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
        if len(result) == 0:
            print("Not found.")
        else:
            md = result2md(result, keyword)
            html = render_html(md)
            with open(HTML_TMP_FILE, 'w') as f:
                f.write(html)
            webbrowser.open(HTML_TMP_FILE)
    else:
        print(result)
