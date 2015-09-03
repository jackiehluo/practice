class Solution(object):
    def removeNthFromEnd(self, head, n):
        start = ListNode(0);
        start.next = head;
        fast = start;
        for i in range(n):
            if fast: fast = fast.next
        if not fast or n == 0: return head
        slow = start
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return start.next