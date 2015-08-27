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

def add_numbers(a, b):
    cur_a, cur_b = a.head, b.head
    total, place, remainder = 0, 1, 0
    while cur_a or cur_b:
        if cur_a and cur_b:
            n = cur_a.data + cur_b.data + remainder
            total += (n % 10) * place
            if n >= 10: remainder = n - 9
            else: remainder = 0
            cur_a, cur_b = cur_a.next, cur_b.next
        elif cur_a:
            total += cur_a.data * place
            cur_a = cur_a.next
        else:
            total += cur_b.data * place
            cur_b = cur_b.next
        place *= 10
    return total

a = LinkedList()
a.insert(8)
a.insert(2)
a.insert(7)

b = LinkedList()
b.insert(4)
b.insert(2)
b.insert(5)
b.insert(1)

print add_numbers(a, b)