from math import comb

for t in range(int(input())):
    n, m = map(int, input().split())
    print(comb(m ,n))

# M개의 지역에 N개의 다리를 놓는 경우의 수
# factorial[M] // (factorial[N] * factorial[M-N])