class Tag:

    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.children = []

    def serialize(self):
        html, stack, open_tags = "", [self], []
        while stack:
            cur = stack.pop()
            if cur.children:
                html += "<%s" % (cur.name)
                for attr, val in cur.attributes.items():
                    html += " %s=%s" % (attr, val)
                html += ">"
                open_tags.append(cur.name)
                for child in cur.children[::-1]:
                    if type(child) == str:
                        html += child
                    else:
                        stack.append(child)
            else:
                html += "<%s/>" % (cur.name)
        for tag in open_tags:
            html += "</%s>" % (tag.name)
        return html