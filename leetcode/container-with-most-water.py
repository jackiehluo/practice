class Solution(object):
   def maxArea(self, height):
       max_area, start, end = 0, 0, len(height) - 1
       while start < end:
           area = (end - start) * min(height[start], height[end])
           if area > max_area: max_area = area
           if height[start] > height[end]: end -= 1
           else: start += 1
       return max_area
