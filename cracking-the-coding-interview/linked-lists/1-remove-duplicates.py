class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node


    def remove_duplicates(self):
        if self.head == None:
            return
        cur = self.head
        while cur != None:
            runner = cur
            while runner.next != None:
                if runner.next.data == cur.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur != None:
            print cur.data
            cur = cur.next


class Node:

    def __init__(self, data, next): 
        self.data = data 
        self.next = next 

    def __str__(self): 
        return str(self.data)

test = LinkedList()

test.insert(6)
test.insert(5)
test.insert(4)
test.insert(8)
test.insert(5)

test.remove_duplicates()
test.print_list()