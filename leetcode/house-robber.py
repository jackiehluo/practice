class Solution(object):
    def rob(self, nums):
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        total, cur = max(nums[0], nums[1]), nums[0]
        for i in range(2, len(nums)):
            cur, next = total, cur
            total = max(nums[i] + next, cur);
        return total