import sys

input =sys.stdin.readline

n = int(input()) # 로프의 개수 n
ropes = []

for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse = True)

for i in range(n):
    ropes[i] = ropes[i] * (i + 1)

print(max(ropes))

# k개의 로프로 중량이 w인 물체를 들어올릴 때, 각 로프에는 w/k의 중량이 걸림
# 내림차순으로 정렬 했을 때 ropes[0] 의 1배의 중량을, ropes[1]의 2배의 중량을,
# ropes[2]의 3배의 중량을, ropes[n]의 (n + 1)배의 중량을 들 수 있음
# 이런식으로 가장 큰 값을 찾으면 됨