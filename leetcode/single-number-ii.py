from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        counts = Counter(nums)
        for k, v in counts.items():
            if v != 3: return k