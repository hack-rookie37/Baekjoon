from math import factorial

for t in range(int(input())):
    n, m = map(int, input().split())
    print(int(factorial(m) / (factorial(n) * factorial(m - n))))

# M개의 지역에 N개의 다리를 놓는 경우의 수
# factorial[M] // (factorial[N] * factorial[M-N])