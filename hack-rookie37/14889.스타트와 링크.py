import sys
from itertools import combinations as cbn, permutations as pmt

input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
MAX = float("inf")


# matrix
def sol1():
    nS = [sum(i) + sum(j) for i, j in zip(S, zip(*S))]
    aS = sum(nS) // 2

    mini = MAX
    for x in cbn(nS[:-1], N // 2):
        mini = min(mini, abs(aS - sum(x)))

    print(mini)


# burte_force
def sol2():
    mini = MAX

    for case in cbn(range(N), N // 2):
        start = set(case)
        link = set(range(N)) - start

        start, link = tuple(start), tuple(link)
        t_start = t_link = 0

        for p, q in pmt(start, 2):
            t_start += S[p][q]
        for p, q in pmt(link, 2):
            t_link += S[p][q]

    mini = min(mini, abs(t_start - t_link))
    print(mini)
