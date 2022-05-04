import sys

input = sys.stdin.readline

n, c = map(int, input().split()) # 집의 개수 n, 공유기의 개수 c
line = sorted([int(input()) for _ in range(n)])

answer = 0
start = 1
end = line[-1] - line[0]

while start <= end:
    mid = (start + end) // 2
    current = line[0] # 마지막으로 설치된 공유기의 위치
    count = 1
    
    for i in range(1, n):
        if line[i] >= current + mid: # current에서 최소 mid 이상의 거리가 떨어진 곳일 때만 공유기 설치
            count += 1
            current = line[i]
    
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

# 최소거리(start) 최대거리(line[-1] - line[0])의 중간 값인 mid를 구하고 
# 그 mid 값보다 거리가 멀 때만 공유기를 설치할 수 있음.
# 모든 설치가 끝난 후 설치된 공유기의 수(count)가 c보다 적다면, end에 mid - 1을 넣어 간격을 좁히고,
# count가 c보다 크다면 start에 mid + 1을 넣어 간격을 넓힘 
