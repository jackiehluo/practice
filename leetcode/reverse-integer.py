class Solution(object):
    def reverse(self, x):
        a, b = str(abs(x)), ""
        for i in range(len(a) - 1, -1, -1):
            b += a[i]
        if int(b) > 2147483647: return 0
        elif x >= 0: return int(b)
        else: return -int(b)