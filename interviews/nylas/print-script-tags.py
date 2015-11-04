def print_script_tags(dependencies, rootfile):
    tags = [rootfile]
    find_dependencies(dependencies, rootfile, tags)
    for tag in tags[::-1]:
        print "<script src=\"%s\">" % tag

def find_dependencies(dependencies, rootfile, tags):
    d = dependencies(rootfile)
    if not d:
        tags.append(rootfile)
    else:
        for d in dependencies(rootfile):
            tags.append(d)
            find_dependencies(d)