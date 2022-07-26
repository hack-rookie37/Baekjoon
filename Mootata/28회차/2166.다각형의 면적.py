n = int(input())
x, y = [], []
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

for i in range(n):
    answer += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

print(round(abs(answer) / 2, 1))

# 신발끈 정리