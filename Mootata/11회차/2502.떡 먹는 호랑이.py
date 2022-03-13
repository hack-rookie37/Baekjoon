import sys

input = sys.stdin.readline

d, k = map(int, input().split()) # 할머니가 넘어온 날 d, 그 날 호랑이에게 준 떡의 개수 k

dp = [0] * d
dp[d - 1] = k

def fibo(n):
    if n <= 1:
        return 1;
    else:
        return fibo(n - 1) + fibo(n - 2)

def sol1():
    for i in range(d - 2, -1, -1):
        for j in range(k//2, -1 ,-1):
            dp = [0] * d
            dp[d - 1] = k
            dp[i] = dp[i + 1] - j
            for l in range(d - 3, -1, -1):
                dp[l] = dp[l + 2] - dp[l + 1]
                if dp[l] >= dp[l + 1]:
                    break
                if 0 < dp[0] < dp[1]:
                    print(dp[0], dp[1], sep='\n')
                    sys.exit(0)

def sol2():
    x = fibo(d - 3)
    y = fibo(d - 2)
    for i in range(k):
        for j in range(k):
            if (x * i + y * j) == k and i < j:
                print(i, j, sep='\n')
                sys.exit(0)

sol2()

# x, y, x+y, x+2y, 2x+3y, 3x+5y
# 2, 7, 9, 16, 25, 41
# 10, 21, 31, 52, 83, 135, 218
# 2, 26, 28, 54, 82, 136, 218
# dp[i - 2] = dp[i] - dp[i - 1]
