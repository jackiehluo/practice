class Solution(object):
    def numTrees(self, n):
        count = [1, 1, 2]
        if n <= 2: return count[n]
        count.extend([0 for i in range(n - 2)])
        for i in range(3, n + 1):
            for j in range(1, i + 1):
                count[i] += count[j - 1] * count[i - j]
        return count[n]