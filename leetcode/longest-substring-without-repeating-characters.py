class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p = {}
        ind, r = -1, 0
        for i in range(len(s)):
            if s[i] in p and ind < p[s[i]]: ind = p[s[i]]
            if i - ind > r: r = i - ind
            p[s[i]] = i
        return r