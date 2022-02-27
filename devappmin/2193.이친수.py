import sys

n = int(sys.stdin.readline())

def solution_with_memory_overflow():
    dp = [["1"]]

    for idx in range(1, n):
        n_dp = []

        for item in dp[idx - 1]:
            n_dp.append(item + "0")
            if item[-1] != "1":
                n_dp.append(item + "1")
        
        dp.append(n_dp)

    print(len(dp[n - 1]))

def solution():
    dp = [1, 1]

    for idx in range(2, n):
        dp.append(dp[idx - 1] + dp[idx - 2])
    
    print(dp[n - 1])

solution()