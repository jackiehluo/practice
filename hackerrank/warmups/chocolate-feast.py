import sys

def get_chocolates(N, C, M):
    chocolates = N / C
    wrappers = chocolates
    while wrappers >= M:
        new_chocolates = wrappers / M
        wrappers %= M
        chocolates += new_chocolates
        wrappers += new_chocolates
    return chocolates

T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]
    answer = get_chocolates(N, C, M)
    print answer
