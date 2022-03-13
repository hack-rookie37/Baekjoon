from itertools import combinations

n, m = map(int, input().split())

combis = list(combinations([i for i in range(1, n + 1)], m))

for i in combis:
    if len(i) == 1:
        print(i[0])
    else:
        print(*i)