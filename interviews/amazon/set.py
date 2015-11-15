class Set:

    def __init__(self):
        self.table = [[] for _ in range(10)]
        self.count = 0

    def hash(self, n):
        return n % 10

    def add(self, item):
        if item not in self.table[hash(item)]:
            self.table[hash(item)].append(item)
            self.count += 1

    def remove(self, item):
        try:
            self.table[hash(item)].remove(item)
            self.count -= 1
        except IndexError:
            print "That item is not in the set!"

    def count(self):
        return self.count
