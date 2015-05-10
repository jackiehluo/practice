import re

n = raw_input()

if n and re.match('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', n):
    print "True"
else:
    print "False"