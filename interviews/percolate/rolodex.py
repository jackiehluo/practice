from collections import OrderedDict
import json


class Rolodex:

    def __init__(self, input):
        self.input = input


    def output_json(self):

        f = open(self.input, 'r')
        line_count = 0
        output = OrderedDict()
        output['entries'] = []
        output['errors'] = []

        for line in f:
            entry = line.split(', ')
            if entry_type_1(entry):
                info = add_entry_1(entry)
                output['entries'].append(info)
            elif entry_type_2(entry):
                info = add_entry_2(entry)
                output['entries'].append(info)
            elif entry_type_3(entry):
                info = add_entry_3(entry)
                output['entries'].append(info)
            else:
                output['errors'].append(line_count)
            line_count += 1

        output['entries'] = sorted(output['entries'], key=lambda k: (k['lastname'], k['firstname']))

        with open('result.out', 'w') as newfile:
            json.dump(output, newfile, indent = 2)


    def entry_type_1(entry):

        return (len(entry) == 5 and entry[0].isalpha() and not
            entry[1].isdigit() and not entry[2].isalpha() and 
            len(entry[2]) == 14 and not entry[3].isdigit() and not
            entry[4].isalpha() and len(entry[4]) == 6)


    def entry_type_2(entry):

        return (len(entry) == 5 and not entry[0].isdigit() and
            entry[1].isalpha() and entry[2].isdigit() and
            len(entry[2]) == 5 and not entry[3].isalpha() and
            len(entry[3]) == 12 and not entry[4].isdigit())


    def entry_type_3(entry):

        return (len(entry) == 4 and not entry[0].isdigit() and not
            entry[1].isdigit() and entry[2].isdigit() and
            len(entry[2]) == 5 and not entry[3].isalpha() and
            len(entry[3]) == 13)


    def add_entry_1(entry):

        info = OrderedDict()
        info['color'] = entry[3]
        info['firstname'] = entry[1]
        info['lastname'] = entry[0]
        num = ''
        for c in entry[2]:
            if c.isdigit():
                num += c
        info['phonenumber'] = '-'.join([num[:3], num[3:6], num[6:]])
        info['zipcode'] = entry[4][:-1]
        return info


    def add_entry_2(entry):

        info = OrderedDict()
        info['color'] = entry[4][:-1]
        info['firstname'] = entry[0]
        info['lastname'] = entry[1]
        info['phonenumber'] = '-'.join(entry[3].split())
        info['zipcode'] = entry[2]
        return info


    def add_entry_3(entry):

        info = OrderedDict()
        info['color'] = entry[1]
        name = entry[0].split()
        info['firstname'] = ' '.join(name[:-1])
        info['lastname'] = name[-1]
        info['phonenumber'] = '-'.join(entry[3][:-1].split())
        info['zipcode'] = entry[2]
        return info


if __name__ == '__main__':

    rolodex = Rolodex('data.in')
    rolodex.output_json