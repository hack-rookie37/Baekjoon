li = (300, 60, 10)
ans = [0, 0, 0]
remain = int(input())

for idx in range(3):
    ans[idx] = remain // li[idx]
    remain %= li[idx]

print(-1) if remain else print(*ans)