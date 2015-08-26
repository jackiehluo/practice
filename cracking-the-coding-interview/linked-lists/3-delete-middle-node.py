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

    def delete_node(self, node):
        node.data = node.next.data
        node.next = node.next.next

class Node:

    def __init__(self, data, next): 
        self.data = data 
        self.next = next

l = LinkedList()
l.insert(8)
l.insert(2)
l.insert(7)
n = l.insert(12)
l.insert(3)
l.insert(4)

l.print_list()
l.delete_node(n)
l.print_list()