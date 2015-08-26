class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next

    def get_kth_to_last(self, k):
        p1 = self.head
        p2 = self.head
        for _ in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1.next.data

class Node:

    def __init__(self, data, next): 
        self.data = data 
        self.next = next

l = LinkedList()
l.insert(8)
l.insert(2)
l.insert(7)
l.insert(12)
l.insert(3)
l.insert(4)

l.print_list()
print l.get_kth_to_last(3)