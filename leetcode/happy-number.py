class Solution(object):
    def isHappy(self, n):
        for _ in range(50):
            if sum(map(int, str(n))) == 1: return True
            n = sum([int(d) ** 2 for d in str(n)])
        return False