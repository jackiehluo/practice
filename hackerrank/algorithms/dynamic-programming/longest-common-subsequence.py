def longest_common_subsequence(n, m, a, b):
    dp = [[0] * (m + 1)] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    lcs = []
    while n > 0 and m > 0:
        if a[n - 1] == b[m - 1]:
            lcs.append(a[n - 1])
            n -= 1
            m -= 1
        elif dp[n - 1][m] >= dp[n][m - 1]:
            n -= 1
        else:
            m -= 1
    return lcs

n, m = map(int, raw_input().split())
a = list(map(int, raw_input().split()))
b = list(map(int, raw_input().split()))
print " ".join(map(str, longest_common_subsequence(n, m, a, b)))