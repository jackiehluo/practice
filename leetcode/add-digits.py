class Solution(object):
    def addDigits(self, num):
        if len(str(num)) == 1: return num
        return self.addDigits(sum(list(map(int, list(str(num))))))