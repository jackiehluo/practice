from collections import OrderedDict
import json

f = open('data.in', 'r')
line_count = 0
output = OrderedDict()
output['entries'] = []
output['errors'] = []

for line in f:
    entry = line.split(', ')
    info = OrderedDict()
    if len(entry) == 5:
        if (entry[0].isalpha() and not entry[1].isdigit() and not
            entry[2].isalpha() and len(entry[2]) == 14 and not
            entry[3].isdigit() and not entry[4].isalpha() and
            len(entry[4]) == 6):
            info['color'] = entry[3]
            info['firstname'] = entry[1]
            info['lastname'] = entry[0]
            num = ''
            for c in entry[2]:
                if c.isdigit():
                    num += c
            info['phonenumber'] = '-'.join([num[:3], num[3:6], num[6:]])
            info['zipcode'] = entry[4][:-1]
            output['entries'].append(info)
        elif (not entry[0].isdigit() and entry[1].isalpha() and
            entry[2].isdigit() and len(entry[2]) == 5 and not
            entry[3].isalpha() and len(entry[3]) == 12 and not
            entry[4].isdigit()):
            info['color'] = entry[4][:-1]
            info['firstname'] = entry[0]
            info['lastname'] = entry[1]
            info['phonenumber'] = '-'.join(entry[3].split())
            info['zipcode'] = entry[2]
            output['entries'].append(info)
        else:
            output['errors'].append(line_count)
    elif len(entry) == 4:
        if (not entry[0].isdigit() and not entry[1].isdigit() and
            entry[2].isdigit() and len(entry[2]) == 5 and not
            entry[3].isalpha() and len(entry[3]) == 13):
            info['color'] = entry[1]
            name = entry[0].split()
            info['firstname'] = ' '.join(name[:-1])
            info['lastname'] = name[-1]
            info['phonenumber'] = '-'.join(entry[3][:-1].split())
            info['zipcode'] = entry[2]
            output['entries'].append(info)
        else:
            output['errors'].append(line_count)
    else:
        output['errors'].append(line_count)
    line_count += 1

output['entries'] = sorted(output['entries'], key=lambda k: (k['lastname'], k['firstname']))

with open('result.out', 'w') as newfile:
    json.dump(output, newfile, indent = 2)