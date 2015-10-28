from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        return [k for k, v in Counter(nums).items() if v == 1]