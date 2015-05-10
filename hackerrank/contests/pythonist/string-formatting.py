n = int(raw_input())
l = len("{0:b}".format(n))

for i in range(1, n + 1):
    print '%(decimal) ls %(octal) ls %(hex) ls %(binary) ls' % \
        {"decimal": str(i).rjust(l), "octal": oct(i)[1:].rjust(l), \
         "hex": format(i, 'X').rjust(l), "binary": "{0:b}".format(i).rjust(l)}