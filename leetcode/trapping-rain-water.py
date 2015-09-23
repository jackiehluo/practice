class Solution(object):
    def trap(self, height):
        if not height or len(height) <= 2: return 0
        max_left, max_right = [0] * len(height), [0] * len(height)
        max_left[0], max_right[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
            max_right[-i] = max(height[-i], max_right[-i + 1])
        units = 0
        for i in range(1, len(height)):
            units += min(max_left[i], max_right[i]) - height[i]
        return units
