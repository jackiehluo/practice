class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2: return len(nums)
        cur = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[cur - 2]:
                nums[cur] = nums[i]
                cur += 1
        return cur