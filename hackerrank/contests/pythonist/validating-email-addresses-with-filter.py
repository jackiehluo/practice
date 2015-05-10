import re

def validate(email):
    try:
        address = email.split('@')
        wn, ext = address[1].split('.')
    except:
        return False
    return (len(address) == 2 and re.match('^[A-Za-z0-9_-]+$', address[0]) and
            re.match('^[A-Za-z0-9]+$', wn) and len(ext) <= 3)

emails = []

for _ in range(input()):
    emails.append(raw_input())

print sorted(list(filter(validate, emails)))