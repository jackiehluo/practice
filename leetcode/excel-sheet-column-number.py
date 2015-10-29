class Solution(object):
    def titleToNumber(self, s):
        num = 0
        for c in s:
            num = num * 26 + ord(c) - 64
        return num