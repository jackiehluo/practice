class Solution(object):
    def searchInsert(self, nums, target):
        if nums[0] > target: return 0
        for i, n in enumerate(nums):
            if n >= target: return i
        return len(nums)