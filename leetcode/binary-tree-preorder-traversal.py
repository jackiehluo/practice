class Solution(object):
    def preorderTraversal(self, root):
        traversal = []
        self.traverse(root, traversal)
        return traversal
    
    def traverse(self, root, traversal):
        if not root: return
        traversal.append(root.val)
        self.traverse(root.left, traversal)
        self.traverse(root.right, traversal)