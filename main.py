#!/usr/bin/env python3
import os
import sys
import json
import webbrowser
import datetime

from jj import startup_behaviour, Action, HELP_TEXT
from search import search_for
from tomd import result2md
from mdformat import render_html


HTML_TMP_FILE = '/tmp/search_result.html'
EDIT_TMP_FILE = '/tmp/jj.txt'
HTML_TEMPLATE = 'template.html'


def load_journal(journal_path):
    with open(journal_path) as f:
        return json.loads(f.read())


def save_journal(journal, journal_path):
    with open(journal_path, 'w') as f:
        return f.write(json.dumps(journal, indent=2))


def today():
    now = datetime.datetime.now()
    return datetime.date(now.year, now.month, now.day)


if __name__ == '__main__':
    args = sys.argv[1:]
    journal_path = os.environ.get('JOURNAL', None)
    result = startup_behaviour(args, journal_path)

    if result == Action.EDIT:
        journal = load_journal(journal_path)
        date = today().strftime("%Y-%m-%d")
        if date not in journal:
            journal[date] = "short desc - longer desc\n   some\n   code"
        with open(EDIT_TMP_FILE, 'w') as f:
            f.write(journal[date])
        os.system('gedit ' + EDIT_TMP_FILE)
        with open(EDIT_TMP_FILE) as f:
            entry = f.read()
        journal[date] = entry
        save_journal(journal, journal_path)

    elif result == Action.SEARCH:
        keyword = sys.argv[1]
        journal = load_journal(journal_path)
        result = search_for(keyword, journal)
        if len(result) == 0:
            print("Not found.")
        else:
            with open(HTML_TEMPLATE) as f:
                template = f.read()
            md = result2md(result, keyword)
            html_body = render_html(md)
            html = template.replace("{{ content }}", html_body)
            with open(HTML_TMP_FILE, 'w') as f:
                f.write(html)
            webbrowser.open(HTML_TMP_FILE)

    else:
        print(result)
