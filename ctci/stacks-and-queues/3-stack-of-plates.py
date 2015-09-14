class Stack(object):

    def __init__(self):
        self.stack = []

    def print_stack(self):
        print self.stack

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        if not self.stack:
            raise Exception('That stack is empty.')
        v, self.stack[-1] = self.stack[-1], None
        return v

class SetOfStacks(object):

    def __init__(self, stack_size):
        self.set = []
        self.stack_size = stack_size

    def push(self, v):
        if not self.set or len(self.set[-1].stack) == self.stack_size:
            cur = Stack()
            self.set.append(cur)
        self.set[-1].push(v)

    def pop(self):
        if not self.set:
            raise Exception('This set of stacks is empty.')
        v = self.set[-1].pop()
        if not self.set[-1].stack:
            self.set.pop()
        return v

    def pop_at(self, ind):
        if ind < 0 or ind > len(self.set) - 1:
            raise Exception('No stack exists at that index.')
        v = self.set[ind].pop()
        return v

s = SetOfStacks(2)
s.push(4)
s.push(2)
s.push(7)
s.push(3)
print s.pop()
print s.pop_at(0)