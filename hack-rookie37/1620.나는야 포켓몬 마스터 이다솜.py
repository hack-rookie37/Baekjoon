import sys

input = sys.stdin.readline

N, M = map(int, input().split())
d = dict()
answer = []

for i in range(1, N + 1):
    name = input().rstrip()
    d[name] = i
    d[i] = name

for j in range(1, M + 1):
    q = input().rstrip()
    try:
        q = int(q)
    except:
        pass

    answer.append(d[q])

print(*answer, sep="\n")
