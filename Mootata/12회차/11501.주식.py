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


# max를 이용해 주가가 가장 높은 날을 찾고, 그 전 날까지는
# answer에 (가장 높은 주가) - (당일 주가) 값을 더해줌
# 주가가 가장 높은 날이 지나면, 그 날 이후의 가장 높은 주가와, 가장 낮은 주가를 구함
# 만약 두 주가가 같다면, 더이상의 이득은 볼 수 없으므로 answer 출력 후 다음 TC로 넘어가고
# 같지 않다면, 주석 1 ~ 2번째 줄을 반복 함.