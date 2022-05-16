n, l = map(int, input().split()) # 물이 새는 곳의 개수 N, 테이프의 길이 L
pipes = sorted(list(map(int, input().split())))
answer = 1
left = pipes[0]
right = left + l

for i in pipes:
    if i < right:
        continue
    else:
        left = i
        right = left + l
        answer += 1

print(answer)