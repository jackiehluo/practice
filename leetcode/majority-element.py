from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        for k, v in counts.items():
            if v > len(nums) / 2: return k