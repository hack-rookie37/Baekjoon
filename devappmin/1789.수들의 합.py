s = int(input())

idx, ans = 1, s
for idx in range(1, s):
    if idx > ans:
        idx -= 1
        break
    ans -= idx

print(idx) 