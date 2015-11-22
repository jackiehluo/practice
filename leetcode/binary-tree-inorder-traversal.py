class Solution(object):
    def inorderTraversal(self, root):
        traversal = []
        self.recursiveInorder(root, traversal)
        return traversal
    
    def recursiveInorder(self, root, traversal):
        if root:
            self.recursiveInorder(root.left, traversal)
            traversal.append(root.val)
            self.recursiveInorder(root.right, traversal)