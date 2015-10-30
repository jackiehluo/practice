class Solution(object):
    def missingNumber(self, nums):
        diff = list(set(range(max(nums))) - set(nums))
        if diff: return diff[0]
        return max(nums) + 1