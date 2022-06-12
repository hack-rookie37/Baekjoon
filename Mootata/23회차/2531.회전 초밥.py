import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # 접시의 수 N, 초밥의 가짓수 D, 연속해서 먹는 접시의 수 K, 쿠폰 번호 C
sushi = [int(input()) for _ in range(n)]
dic = defaultdict(int)
dic[c] += 1 # 쿠폰으로 받는 초밥은 무조건 먹음
l = len(sushi)
start, end = 0, k

for i in range(k): # 연속해서 k개를 먹음
    dic[sushi[i]] += 1

answer = len(dic)

while start < l:
    dic[sushi[start]] -= 1
    
    if dic[sushi[start]] == 0:
        del dic[sushi[start]]
    
    dic[sushi[end % n]] += 1 # 회전 초밥이라 리스트의 끝과 처음이 연결되어 있으므로 end는 l을 넘으면 다시 0 ~ k - 1까지 증가
    
    answer = max(answer, len(dic))
    
    start += 1
    end += 1

print(answer)