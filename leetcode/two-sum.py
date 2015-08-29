class Solution(object):
    def twoSum(self, nums, target):
        n = {}
        for i in range(len(nums)):
            if target - nums[i] in n:
                return n[target - nums[i]] + 1, i + 1
            n[nums[i]] = i