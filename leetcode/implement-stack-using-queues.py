class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        del self.stack[-1]

    def top(self):
        return self.stack[-1]        

    def empty(self):
        return False if self.stack else True