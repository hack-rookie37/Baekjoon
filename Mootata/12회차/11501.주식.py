import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input()) # 날의 수 N
    share_prices = list(map(int, input().split())) # 날짜별 주가
    buy = []
    answer = 0
    min_val = min(share_prices)
    max_val = max(share_prices)
    
    if min_val == max_val: # 주가의 최소, 최대값이 같으면 이익은 없으므로 0 출력 후 다음 TC로 넘어감
        print(answer)
        continue
    
    for i in range(n):
        if share_prices[i] != max_val:
            answer += max_val - share_prices[i]
        else: # 최대 주가 갱신
            if i != n - 1:
                max_val = max(share_prices[i + 1:])
                min_val = min(share_prices[i + 1:])
                if max_val == min_val:
                    break
            else:
                break 
    print(answer)


# max를 이용해 주가가 가장 높은 날을 찾고, 그 전 날까지는 다 산다.
# 주가가 가장 높은 날이 되면 모든 주식을 판다.
# 주식을 팔고, 남은 날짜 중 주가가 가장 높은 날을 찾는다. 만약 주가가 가장 높은날이 당일이라면
# 아무것도 하지 않고 넘어간 뒤 다시 남은 날 중 주가가 가장 높은 날을 찾는다.
# 만약 주가가 가장 높은 날을 찾았다면 처음과 마찬가지로 그 전날까지 주식을 모두 사고,
# 당일날 판다. 이렇게 반복. 


# 1 1 3 5 2 7 2 2 2 2 2 3