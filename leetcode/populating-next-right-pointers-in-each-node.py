class Solution(object):
    def connect(self, root):
        if not root or not root.left and not root.right:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)