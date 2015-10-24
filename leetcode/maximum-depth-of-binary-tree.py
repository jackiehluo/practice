class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1