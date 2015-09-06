class Solution(object):
    def intToRoman(self, num):
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        r = ""
        for i in range(len(ints)):
            while num >= ints[i]:
                num -= ints[i]
                r += numerals[i]
        return r