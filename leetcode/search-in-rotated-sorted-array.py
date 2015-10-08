class Solution(object):
    def search(self, nums, target):
        for i, n in enumerate(nums):
            if target == n: return i
        return -1