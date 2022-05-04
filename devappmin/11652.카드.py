import sys

n = int(sys.stdin.readline())
num_dicts = {}

for _ in range(n):
    i = int(sys.stdin.readline())
    num_dicts[i] = 1 if i not in num_dicts else num_dicts[i] + 1
    
ans, idx = 0, 0
for k, v in num_dicts.items():
    if v > ans:
        ans = v
        idx = k
    elif v == ans:
        idx = min(idx, k)
print(idx)