class Solution(object):
    def isBalanced(self, root):
        if not root: return True
        return (abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and
                self.isBalanced(root.left) and self.isBalanced(root.right))

    def getHeight(self, root):
        if not root: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1