class Solution(object):
    def productExceptSelf(self, nums):
        left = 1
        output = [1] * len(nums)
        for i in range(len(nums) - 1):
            left *= nums[i]
            output[i + 1] *= left
        right = 1
        for i in range(len(nums) - 1, 0, -1):
            right *= nums[i]
            output[i - 1] *= right
        return output