n = int(input()) # 퇴사까지 남은 날짜 n
tp = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

def sol1(): # 앞에서 부터
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        t, p = tp[i]
        dp[i] = max(dp[i], dp[i - 1])
        if i + t - 1 <= n: # i일에 있는 스케쥴을 진행했을 때 퇴사일 이전에 상담이 완료 되는 경우
            dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)
            # i일에 시작한 상담이 끝나는 날의 임금은
            # i - 1일까지의 최대 임금과 이번 상담의 임금을 더한 값 중 큰 값을 넣어줌

    print(dp[-1])

def sol2(): # 뒤에서 부터
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        t, p = tp[i]
        if i + t > n: # 퇴사일보다 상담이 오래 걸린다면
            dp[i] = dp[i + 1] # 다음날의 임금을 그대로 가져옴
        else: # 상담을 할 수 있다면
            dp[i] = max(dp[i + 1], p + dp[i + t]) # 다음날의 임금과 (오늘 임금 + t일 이후의 임금) 중 큰것을 저장
    print(dp[0])

sol1()