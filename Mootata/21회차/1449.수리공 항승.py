n, l = map(int, input().split()) # 물이 새는 곳의 개수 N, 테이프의 길이 L
pipes = sorted(list(map(int, input().split())))
answer = 1
left = pipes[0] # 테이프가 붙는 첫번째 지점
right = left + l # 테이프의 끝 부분

for i in pipes:
    if i < right: # 마지막에 붙인 테이프의 끝 부분보다 짧은 거리에 있다면 더 붙일 필요 없음
        continue
    else: # 마지막에 붙인 테이프의 끝 부분보다 긴 거리에 있다면 해당 위치에 테이프를 붙임
        left = i
        right = left + l
        answer += 1

print(answer)