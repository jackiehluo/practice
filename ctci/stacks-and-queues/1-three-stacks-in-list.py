class Stack(object):

    def __init__(self, size):
        self.size = size
        self.stack = [None] * size * 3
        self.pointers = [-1, -1, -1]

    def print_list(self):
        print self.stack

    def top(self, n):
        return n * self.size + self.pointers[n]

    def is_empty(self, n):
        return self.pointers[n] == -1

    def push(self, n, v):
        if self.pointers[n] + 1 >= self.size:
            raise Exception('That stack is full.')
        self.pointers[n] += 1
        self.stack[self.top(n)] = v

    def pop(self, n):
        if self.is_empty(n):
            raise Exception('That stack is empty.')
        v = self.stack[self.top(n)]
        self.stack[self.top(n)] = None
        self.pointers[n] -= 1
        return v

    def peek(self, n):
        if self.is_empty(n):
            raise Exception('That stack is empty.')
        return self.stack[self.top(n)]

s = Stack(10)
s.push(0, 5)
s.push(0, 2)
s.push(0, 7)
s.push(1, 3)
s.push(1, 9)
s.push(1, 8)
s.push(2, 3)
s.push(2, 7)
s.push(2, 5)
s.print_list()
s.pop(2)
s.print_list()