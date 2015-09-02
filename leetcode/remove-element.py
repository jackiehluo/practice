class Solution(object):
    def removeElement(self, nums, val):
        j = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j + 1