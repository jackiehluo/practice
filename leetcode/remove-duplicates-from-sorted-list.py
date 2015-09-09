class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val: cur.next = cur.next.next
            else: cur = cur.next
        return head