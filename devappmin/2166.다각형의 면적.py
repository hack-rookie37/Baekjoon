import sys

n = int(sys.stdin.readline())
xs, ys = [], []
answer = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

xs, ys = [*xs, xs[0]], [*ys, ys[0]]

for idx in range(n):
    answer += xs[idx] * ys[idx + 1] - xs[idx + 1] * ys[idx]

print("{:.1f}".format(abs(answer / 2)))

# 신발끈 정리
# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B