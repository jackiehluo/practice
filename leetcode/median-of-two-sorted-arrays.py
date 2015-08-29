class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       n = sorted(nums1 + nums2)
       mid = len(n) / 2
       if len(n) % 2 == 0:
           return (n[mid - 1] + n[mid]) / 2.0
       else:
           return n[mid]
