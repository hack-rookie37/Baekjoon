import sys

n, k = map(int, sys.stdin.readline().split())
nums = [False, False] + [True] * (n - 1)
ans = 0

for idx in range(2, n + 1):
    for i in range(idx, n + 1, idx):
        if nums[i]:
            nums[i] = False
            ans += 1
        
            if ans == k:
                print(i)
                exit(0)