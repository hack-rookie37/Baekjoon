import sys

input = sys.stdin.readline

N = int(input())
tower = [int(input()) for _ in range(N)]
total = sum(tower)


answer = e = p = 0

for s in range(N):
    dist = [0, 0]
    while e < N:
        p += tower[e]
        q = total - p

        if min(p, q) > min(dist):
            dist[0], dist[1] = p, q

        if p >= q:
            break

        e += 1

    answer = max(answer, min(dist))

    if e < N:
        p -= tower[e] + tower[s]

print(answer)
