class Stack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('The stack is empty.')
        return self.stack[-1]

def sort_stack(s):
    r = Stack()
    while not s.is_empty():
        cur = s.pop()
        while not r.is_empty() and r.peek() > cur:
            s.push(r.pop())
        r.push(cur)
    return r.stack

s = Stack()
s.stack = [2, 5, 7, 1, 4, 6, 8, 3, 5, 4]
print(sort_stack(s))