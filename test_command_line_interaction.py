#coding: utf-8

import json
import unittest

from jj import startup_behaviour, Action, HELP_TEXT




class TestCommandLine(unittest.TestCase):

    def test_journal_not_set(self):
        self.assertEqual(HELP_TEXT, startup_behaviour(
            args=[],
            journal_path=None
        ))

    def test_journal_set_no_args_opens_editor(self):
        self.assertEqual(Action.EDIT, startup_behaviour(
            args=[],
            journal_path='/tmp/tmp.json'
        ))

    def test_journal_set_single_argument_searches(self):
        self.assertEqual(Action.SEARCH, startup_behaviour(
            args=['git'],
            journal_path='/tmp/tmp.json'
        ))

    def test_journal_set_multi_arguments_prints_informative_error_message(self):
        self.assertEqual("Only single keyword search supported.", startup_behaviour(
            args=['multi', 'args'],
            journal_path='/tmp/tmp.json'
        ))

