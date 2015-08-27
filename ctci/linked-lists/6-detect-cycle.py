class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.last = None

    def insert_at_end(self, data, next=None):
        node = Node(data, next)
        if self.head and self.last:
            self.last.next = node
            self.last = node
        else:
            self.head, self.last = node, node
        return node

    def print_list(self):
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next

class Node:

    def __init__(self, data, next): 
        self.data = data 
        self.next = next

def detect_cycle(l):
    slow, fast = l.head, l.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = l.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast.data
    return None

l = LinkedList()
l.insert_at_end(4)
l.insert_at_end(6)
start = l.insert_at_end(2)
l.insert_at_end(5)
l.insert_at_end(1)
l.insert_at_end(8, start)

print detect_cycle(l)