def search_for_inner(keyword, journal):
    for date in journal:
        entry = journal[date]
        if keyword in entry or keyword in date:
            yield (date, entry)


def search_for(keyword, journal):
    return sorted(
    	list(search_for_inner(keyword, journal)),
    	reverse=True
    )
