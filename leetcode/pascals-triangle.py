class Solution(object):
    def generate(self, numRows):
        if numRows == 0: return []
        triangle, row = [[1]], [1]
        for i in range(1, numRows):
            prev = row
            row = [1]
            for j in range(0, i - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            triangle.append(row)
        return triangle