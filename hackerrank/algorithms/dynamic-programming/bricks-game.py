def find_max_score(bricks):
    n = len(bricks)
    if n <= 3:
        return sum(bricks)
    scores = [sum(bricks[n - 3:]), sum(bricks[n - 2:]), bricks[-1]]
    end = scores[0]
    for i in range(n - 4, -1, -1):
        cur = bricks[i] + end - min(scores)
        scores.pop()
        scores.insert(0, cur)
        end += bricks[i]
    return scores[0]

for _ in range(int(raw_input())):
    n = int(raw_input())
    bricks = list(map(int, raw_input().split()))
    print find_max_score(bricks)