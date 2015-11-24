class Solution(object):
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return True
        return False