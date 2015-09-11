class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        start, cur, prev = head.next, head, None
        while cur and cur.next:
            if prev: prev.next = cur.next
            prev, cur.next.next, cur.next = cur, cur, cur.next.next
            cur = cur.next
        return start