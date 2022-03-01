n = int(input()) # 자연수 n
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1 :
            dp[i] = dp[i - j * j] + 1

print(dp[n])

# 1 = 1,
# 2 = 2,
# 3 = 3,
# 4 = 1, 
# 5 = 2,
# 6 = 3,
# 7 = 4,
# 8 = 2,
# 9 = 1,
# 10 = 2,
# 11 = 3,
# 12 = 3,
# 13 = 2, 3^2 + 2^2
# 14 = 3, 
# 15 = 4,
# 16 = 1 