class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
        return self.recurse(root.left, root.right)
    
    def recurse(self, left, right):
        if not left and not right: return True
        elif left and right and left.val == right.val:
            return (self.recurse(left.right, right.left) and
                    self.recurse(left.left, right.right))
        return False