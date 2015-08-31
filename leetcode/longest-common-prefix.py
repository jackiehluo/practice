class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        l = len(strs[0])
        for str in strs[1:]:
            ind = 0
            while ind < len(str) and ind < l and strs[0][ind] == str[ind]:
                ind += 1
            l = min(ind, l)
        return strs[0][:l]