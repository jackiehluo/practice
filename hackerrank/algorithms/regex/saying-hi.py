import re

for _ in range(int(raw_input())):
    s = raw_input()
    if re.match("[hH][iI][ ][^dD].*", s):
        print s