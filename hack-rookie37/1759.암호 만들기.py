from itertools import combinations

L, C = map(int, input().split())
cipher = input().split()

v = tuple(v for v in cipher if v in ("a", "e", "i", "o", "u"))
r = tuple(r for r in cipher if r not in v)
d = []
for i in range(1, L - 1):
    j = L - i
    for x in combinations(v, i):
        for y in combinations(r, j):
            d.append(sorted(list(x + y)))

d = list(map("".join, d))
d.sort()
print(*d, sep="\n")
