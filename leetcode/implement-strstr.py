class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "": return 0
        elif haystack == "": return -1
        ind = 0
        while len(haystack) - ind >= len(needle):
            for i in range(len(needle)):
                if haystack[ind + i] != needle[i]: break
            else: return ind
            ind += 1
        return -1