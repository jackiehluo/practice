class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0
        s = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[s]:
                s += 1
                nums[i], nums[s] = nums[s], nums[i]
        return s + 1