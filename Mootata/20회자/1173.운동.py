n, m, m2, t, r = map(int, input().split())
cnt = t2 = 0
current = m

while cnt < n:
    if m + t > m2:
        break
    if current + t <= m2:
        current += t
        cnt += 1
    else:
        current = max(current - r, m)
    t2 += 1

print(t2 if cnt == n else -1)