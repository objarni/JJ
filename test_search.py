#coding: utf-8

import json
import unittest

from search import search_for

JOURNAL = json.loads(u"""
{
    "2018-01-01": "git co -b branch - bygg och checka ut en branch",
    "2018-06-05": "git pull - ta hem senaste ändringar och uppdatera denna branch",
    "2019-03-05": "git branch - lista branches"
}
""")

class TestSearch(unittest.TestCase):

    def test_no_math(self):
        self.assertEqual([], search_for('hg', JOURNAL))

    def test_one_match(self):
        self.assertEqual(
            [("2018-01-01", "git co -b branch - bygg och checka ut en branch")],
            search_for('bygg', JOURNAL)
        )

    def test_looks_at_dates(self):
        self.assertEqual(
            [("2019-03-05", "git branch - lista branches")],
            search_for('2019', JOURNAL)
        )

    def test_result_is_sorted_on_date_newest_first(self):
        self.assertEqual(
            [
                ("2019-03-05", "git branch - lista branches"),
                ("2018-06-05", u"git pull - ta hem senaste ändringar och uppdatera denna branch"),
                ("2018-01-01", "git co -b branch - bygg och checka ut en branch"),
            ],
            search_for('git', JOURNAL)
        )
