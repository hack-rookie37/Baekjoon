import sys

n, m = map(int, sys.stdin.readline().split())
coords = sorted([int(sys.stdin.readline()) for _ in range(n)])

left, right = 1, coords[-1] - coords[0]

ans = []

while left <= right:
    center = (right + left) // 2;
    
    cnt = 1
    curr = coords[0]

    for coord in coords:
        if curr + center <= coord:
            cnt += 1
            curr = coord
    
    if cnt >= m:
        left = center + 1
        ans.append(center)
        continue

    right = center - 1

print(max(ans))

# 이해한 내용)
# 공유기 개수 3
# 좌표 : 1 2 4 8 9

# 만약
# 거리 = 2 라면
# 1에 설치하면 1+2 = 3   -> 다음 설치할 공유기 위치는 3이상인 좌표이다.
# 2에는 설치 못한다.
# 4에 설치 4+2 = 6 -> 다음 설치할 공유기 위치는 6이상인 좌표이다.
# 8에 설치 8+2 = 10 -> 다음에 설치할 공유기 위치는 10이상인 좌표이다.
# 9에는 설치 못한다.
# 끝----- 설치한 공유기 개수 3개
# 거리가 2일때 만족

# 만약
# 거리 = 3 라면
# 1에 설치하면 1+3 = 4   -> 다음 설치할 공유기 위치는 4이상인 좌표이다.
# 2에는 설치 못한다.
# 4에 설치 4+3 = 7 -> 다음 설치할 공유기 위치는 7이상인 좌표이다.
# 8에 설치 8+3 = 11 -> 다음에 설치할 공유기 위치는 11이상인 좌표이다.
# 9에는 설치 못한다.
# 끝----- 설치한 공유기 개수 3개
# 거리가 3일때 만족