def fermat(a, b):
    if b == 1:
        return a % d
    elif b % 2:
        return a * fermat(a, b - 1) % d
    else:
        p = fermat(a, b // 2)
        return p * p % d

m = int(input())
d = 1000000007
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    answer += b * fermat(a, d - 2) % d
print(answer % d)