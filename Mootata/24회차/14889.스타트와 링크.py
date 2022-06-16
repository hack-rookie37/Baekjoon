from itertools import combinations

n = int(input())
player = list(range(n))
team = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

for s in combinations(player, n // 2):
    l = list(set(player) - set(s))
    start, link = 0, 0
    for i, j in combinations(s, 2):
        start += team[i][j]
        start += team[j][i]
    for i, j in combinations(l, 2):
        link += team[i][j]
        link += team[j][i]
    answer = min(answer, abs(start - link))

print(answer)