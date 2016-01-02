class Solution(object):
    def maxProduct(self, words):
        keys = [0] * len(words)
        for i in range(len(words)):
            for c in words[i]:
                keys[i] |= 1 << ord(c) - ord("a")
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if (keys[i] & keys[j]) == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product