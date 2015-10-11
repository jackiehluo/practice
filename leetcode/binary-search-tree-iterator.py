class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    def hasNext(self):
        return self.stack

    def next(self):
        next = self.stack.pop()
        self.pushLeft(next.right)
        return next.val
    
    def pushLeft(self, cur):
        while cur:
            self.stack.append(cur)
            cur = cur.left