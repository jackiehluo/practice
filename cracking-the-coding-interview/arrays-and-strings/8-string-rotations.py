def is_substring(s1, s2):
    return (s1 in s2) or (s2 in s1)

def is_rotation(s1, s2):
    if len(s1) != len(s2) or not (s1 and s2): return False
    return is_substring(s1 + s1, s2)

s1 = "waterbottle"
s2 = "erbottlewat"
print is_rotation(s1, s2)
