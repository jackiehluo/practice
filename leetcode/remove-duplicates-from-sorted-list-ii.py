class Solution(object):
    def deleteDuplicates(self, head):
        start = ListNode(0)
        start.next = head
        cur = start
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                n = cur.next.val
                while cur.next and cur.next.val == n:
                    cur.next = cur.next.next
            else: cur = cur.next
        return start.next