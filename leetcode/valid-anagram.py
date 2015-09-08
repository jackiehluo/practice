class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        counts = {}
        for c in s:
            if c in counts: counts[c] += 1
            else: counts[c] = 1
        for c in t:
            if c in counts: counts[c] -= 1
            else: return False
            if counts[c] < 0: return False
        return True