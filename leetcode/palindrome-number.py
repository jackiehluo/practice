class Solution(object):
    def isPalindrome(self, x):
        a, b = str(x), ""
        for i in range(len(a) - 1, -1, -1):
            b += a[i]
        return True if a == b else False