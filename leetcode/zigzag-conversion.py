class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1: return s
        zz = [""] * numRows
        ind, step = 0, 1
        for c in s:
            zz[ind] += c
            if ind == numRows - 1: step = -1
            if ind == 0: step = 1
            ind += step
        return "".join(map(str, zz))