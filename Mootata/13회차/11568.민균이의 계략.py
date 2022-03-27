import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input()) # 카드의 개수 n
cards = list(map(int, input().split()))

answer = [float('inf')] * n

for i in range(n):
    index = bisect_left(answer, cards[i]) # answer에서 cards[i]를 insert 할 때 그 위치의 인덱스
    answer[index] = cards[i]

print(bisect_left(answer, float('inf')))

# answer에 어떤 값이 들어가 있느냐가 중요한 게 아니라
# answer에 inf가 아닌 값의 길이가 중요한 것

# 9
# 6 4 5 3 5 6 7 1 2

# 예를 들어 위의 예시의 경우 결국 마지막에 answer에 들어있는 값은 
# [1, 2, 6, 7, inf, inf, inf, inf, inf]
# 입력값에서 1, 2, 6, 7 이라는 순증가 수열은 없지만
# 중요한 것은 어떤 값이 들어 있느냐가 아니라 가장 길었던 순증가 수열의 길이이므로,
# 7까지의 길이인 4가 정답인 것임