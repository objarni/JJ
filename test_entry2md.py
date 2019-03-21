import unittest
import re

RE = re.compile('(.*) - (.*)')

def parse_boldrow(row):
    m = RE.match(row)
    if m:
        return m.groups()
    else:
        return None


def entry2md_inner(entry_lines):
    for line in entry_lines:
        print(line)
        result = parse_boldrow(line)
        if result:
            (boldtxt, desc) = result
            yield "**{}** - {}".format(boldtxt, desc)
        else:
            yield line


def entry2md(entry):
    entry = entry.strip()
    return '\n'.join(entry2md_inner(entry.splitlines()))


class TestToplevel(unittest.TestCase):

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

class TestRegex(unittest.TestCase):

    def test_no_math(self):
        self.assertEqual(None, parse_boldrow('Hejsan hej'))

    def test_math(self):
        self.assertEqual(('git', 'ett dvcs program'), parse_boldrow('git - ett dvcs program'))
