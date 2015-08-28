class Stack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def print_stack(self):
        print self.stack

    def push(self, v):
        self.stack.append(v)
        if not self.min or v < self.min[-1]:
            self.min.append(v)

    def pop(self):
        if not self.stack:
            raise Exception('That stack is empty.')
        v = self.stack[-1]
        if v == self.min[-1]:
            self.min.pop()
        return v

    def stack_min(self):
        return self.min[-1]

s = Stack()
s.push(28)
s.push(83)
print s.stack_min()
s.push(51)
s.push(2)
print s.stack_min()
s.pop()
print s.stack_min()
s.push(14)
s.push(9)
print s.stack_min()
s.push(37)
s.print_stack()