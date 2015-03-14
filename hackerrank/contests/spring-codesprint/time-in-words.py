def tell_time(h, m):
    if m == 0:
        return n[h] + " o' clock"
    elif m == 1:
        return n[m] + " minute past " + n[h]
    elif m == 15:
        return "quarter past " + n[h]
    elif m == 30:
        return "half past " + n[h]
    elif m < 30:
        if m > 20:
            return n[20] + " " + n[m - 20] + " minutes past " + n[h]
        return n[m] + " minutes past " + n[h]
    elif m == 45:
        if h == 12:
            return "quarter to " + n[1]
        return "quarter to " + n[h + 1]
    elif m == 59:
        if h == 12:
            return n[1] + " minute to " + n[1]
        return n[1] + " minute to " + n[h + 1]
    elif m > 30:
        if m < 40:
            if h == 12:
                return n[20] + " " + n[40 - m] + " minutes to " + n[1]
            return n[20] + " " + n[40 - m] + " minutes to " + n[h + 1]
        if h == 12:
            return n[60 - m] + " minutes to " + n[1]
        return n[60 - m] + " minutes to " + n[h + 1]

n = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
}

h = int(raw_input())
m = int(raw_input())
print tell_time(h, m)
