class Solution(object):
    def mergeTwoLists(self, l1, l2):
        start = ListNode(0)
        cur = start
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if not l1: cur.next = l2
        else: cur.next = l1
        return start.next
