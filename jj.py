from enum import Enum

class Action(Enum):
    EDIT = 1
    SEARCH = 2


JJ_EDITOR, JJ_SEARCH = range(2)
HELP_TEXT = """Usage: JJ [keyword]\n\tMake sure JOURNAL env.var points to journal
 in .json format. If keyword is left out, edits todays journal entry. Otherwise,
 display all entries containing keyword."""

def startup_behaviour(args, journal_path):
    if journal_path is None:
        return HELP_TEXT
    if len(args) == 1:
        return Action.SEARCH
    if len(args) > 1:
        return "Only single keyword search supported."
    return Action.EDIT

