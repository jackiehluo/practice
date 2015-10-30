class Solution(object):
    def hammingWeight(self, n):
        return sum([1 for c in list(bin(n)[2:]) if c == "1"])