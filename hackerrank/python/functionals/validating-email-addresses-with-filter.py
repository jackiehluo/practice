import re

n = int(raw_input())
emails = []

for _ in range(n):
    emails.append(raw_input())

m = re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")
print sorted(filter(m.match, emails))
