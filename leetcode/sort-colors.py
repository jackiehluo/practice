from collections import defaultdict

class Solution(object):
    def sortColors(self, nums):
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        ind = 0
        for key, val in sorted(counts.items()):
            nums[ind:ind + val] = [key] * val
            ind += val