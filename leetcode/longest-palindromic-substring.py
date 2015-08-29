class Solution(object):
    def longestPalindrome(self, s):
        def helper(i, j):
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]
        if not s: return None
        elif len(s) == 1: return s
        sub = ""
        for i in range(len(s)):
            a, b = helper(i, i), helper(i, i + 1)
            if len(a) > len(sub): sub = a
            if len(b) > len(sub): sub = b
        return sub