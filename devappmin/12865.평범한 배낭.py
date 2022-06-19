import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = defaultdict(int)
dp[0] = 0

for w, v in items:
    temp = []

    for dw, dv in dp.items():
        if dw + w <= k:
            temp.append((dw + w, dv + v))
    
    for tw, tv in temp:
        if tw in dp and dp[tw] >= tv:
            continue

        dp[tw] = tv

print(max(dp.values()))