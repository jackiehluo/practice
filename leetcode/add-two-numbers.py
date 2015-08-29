class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur = ListNode(0)
        start = cur
        carry = 0
        while l1 or l2 or carry:
            if l1 and l2:
                v = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1:
                v = l1.val + carry
                l1 = l1.next
            elif l2:
                v = l2.val + carry
                l2 = l2.next
            elif carry:
                v = carry
            if v >= 10: carry = 1
            else: carry = 0
            cur.next = ListNode(v % 10)
            cur = cur.next
        return start.next