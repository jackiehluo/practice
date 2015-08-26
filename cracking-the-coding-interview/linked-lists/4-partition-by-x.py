class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        return self.head

    def print_list(self):
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next

class Node:

    def __init__(self, data, next): 
        self.data = data 
        self.next = next

def partition(l, x):
    before = LinkedList()
    after = LinkedList()
    cur, mid = l.head, None
    while cur:
        if cur.data < x:
            if not mid: mid = before.insert(cur.data)
            else: before.insert(cur.data)
        else: after.insert(cur.data)
        cur = cur.next
    mid.next = after.head
    before.print_list()

l = LinkedList()
l.insert(8)
l.insert(2)
l.insert(7)
l.insert(12)
l.insert(3)
l.insert(4)

l.print_list()
partition(l, 5)