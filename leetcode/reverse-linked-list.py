class Solution(object):
    def reverseList(self, head):
        cur = None
        while head:
            head.next, head, cur = cur, head.next, head
        return cur