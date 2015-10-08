class Solution(object):
    def invertTree(self, root):
        queue = [root]
        while queue:
            cur = queue.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                queue.append(cur.left)
                queue.append(cur.right)
        return root