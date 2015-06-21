s = raw_input()
time = s[:-2]

if s[-2:] == "AM":
    if s[:2] == "12":
        time = "00" + time[2:]
else:
    if s[:2] != "12":
        time = str(int(time[:2]) + 12) + time[2:]

print time