#coding: utf-8
import unittest

from test_search import JOURNAL
from search import search_for
from tomd import parse_boldrow, entry2md, result2md, swedate


class TestBoldRowRegex(unittest.TestCase):

    def test_no_math(self):
        self.assertEqual(None, parse_boldrow('Hejsan hej'))

    def test_math(self):
        self.assertEqual(('git', 'ett dvcs program'), parse_boldrow('git - ett dvcs program'))


class TestEntry2md(unittest.TestCase):

    def test_simple_entry(self):
        entry = 'git co -b branch - skapa och checka ut ny branch.'
        expected_md = '**git co -b branch** - skapa och checka ut ny branch.'
        self.assertEqual(expected_md, entry2md(entry))

    def test_entry_with_code_example(self):
        entry = """
    def fn(x, y):
        return 2"""
        expected_md = entry
        self.assertEqual(expected_md.strip(), entry2md(entry).strip())


class TestSearchResult2md(unittest.TestCase):


    def test_single_entry_found(self):
#         expected = """
# Hittade "2019" i följande anteckningar
# ======================================

# Onsdag 5e mars 2019
# -------------------

# **git branch** - lista branches
# """
        expected = """
Hittade "2019" i följande anteckningar
======================================

Tisdag 5e mars 2019
-------------------
"""
        result = search_for('2019', JOURNAL)
        got = result2md(result, '2019')
        self.assertEqual(expected.strip(), got.strip())

class TestNiceSwedishJournalDateFormatting(unittest.TestCase):

    def test_sunday24th_of_march_2019(self):
        self.assertEqual(u"Söndag 24e mars 2019", swedate(2019, 3, 24))

    def test_tuesday2nd_of_april_2019(self):
        self.assertEqual(u"Tisdag 2e april 2019", swedate(2019, 4, 2))

    def test_monday1st_of_april_2019(self):
        self.assertEqual(u"Måndag 1a april 2019", swedate(2019, 4, 1))

    def test_sunday31st_of_march_2019(self):
        self.assertEqual(u"Söndag 31a mars 2019", swedate(2019, 3, 31))
