class MyQueue:

    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, data):
        self.inbox.append(data)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

q = MyQueue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())