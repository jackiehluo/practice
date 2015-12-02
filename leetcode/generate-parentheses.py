class Solution(object):
    def generateParenthesis(self, n):
        dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + first_parens + ')' + second_parens
                          for first_parens in dp[j]
                          for second_parens in dp[i - j - 1]]
        return dp[n]