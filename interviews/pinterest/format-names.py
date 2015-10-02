def format(names, limit):
    formatted_names = ""
    if len(names) == 1: return name[0]
    for n, name in enumerate(names[:limit]):
        if 1 < n < len(names) - 1:
            formatted_names += ", "
        elif n == len(names) - 1:
            formatted_names += " and "
        formatted_names += name
    if limit < len(names):
        formatted_names += " and %d more" % (len(names) - limit)
    return formatted_names