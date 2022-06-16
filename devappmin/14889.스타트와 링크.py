import sys
from itertools import combinations

n = int(sys.stdin.readline())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = float("inf")

for team in combinations(range(n), n // 2):
    start, link = 0, 0
    
    for a, b in combinations(team, 2):
        start += stats[a][b] + stats[b][a]

    for a, b in combinations(set(range(n)) - set(team), 2):
        link += stats[a][b] + stats[b][a]

    answer = min(answer, abs(link - start))    

print(answer)