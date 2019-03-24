#coding: utf-8
import re
import datetime


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


def ulen(s):
    return len(s.decode('utf-8'))


def parse_date(d):
    return map(int, d.split('-'))


def result2md(result, keyword):
    header = 'Hittade "{}" i följande anteckningar'.format(keyword)
    header += '\n' + '=' * ulen(header) + '\n\n'
    body = ""
    for date, entry in result:
        (y, m, d) = parse_date(date)
        datestr = swedate(y, m, d)
        body += '{}\n{}\n\n'.format(datestr, '-' * ulen(datestr))
    return header + body


SWEWEEKDAYS = u'Måndag Tisdag Onsdag Torsdag Fredag Lördag Söndag'.split()
SWEMONTHS = u'januari februari mars april maj juni juli augusti september oktober november december'.split()


def swedate(year, month, day):
    dt = datetime.datetime(year, month, day)
    sweday = SWEWEEKDAYS[dt.weekday()]
    ending = 'a' if day in [1, 31] else 'e'
    swemonth = SWEMONTHS[month - 1]
    return u'{weekday} {day}{end} {month} {year}'.format(
        weekday=sweday,
        day=day,
        end=ending,
        month=swemonth,
        year=year
    )
