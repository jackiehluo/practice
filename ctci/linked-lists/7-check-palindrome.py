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

class Node:

    def __init__(self, data, next): 
        self.data = data 
        self.next = next

def reverse(l):
    reverse = LinkedList()
    cur = l.head
    while cur:
        reverse.insert(cur.data)
        cur = cur.next
    return reverse

def is_palindrome(l):
    r = reverse(l)
    cur_l, cur_r = l.head, r.head
    while cur_l and cur_r:
        if cur_l.data != cur_r.data:
            return False
        cur_l, cur_r = cur_l.next, cur_r.next
    return True

l = LinkedList()
l.insert("h")
l.insert("a")
l.insert("n")
l.insert("n")
l.insert("a")
l.insert("h")
print is_palindrome(l)