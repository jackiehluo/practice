class Solution(object):
    def romanToInt(self, s):
        numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        total, last = 0, 0
        for c in s[::-1]:
            if last and numerals[c] < last:
                total -= numerals[c] * 2
            total += numerals[c]
            last = numerals[c]
        return total