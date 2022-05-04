import sys

n = int(sys.stdin.readline())

dp = [-1000]
for next in list(map(int, sys.stdin.readline().split())):
    dp.append(max(next, dp[-1] + next))


print(max(dp))