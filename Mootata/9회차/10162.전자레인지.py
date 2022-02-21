t = int(input()) # 요리시간 t
answer = [0, 0, 0]

answer[0] = t // 300
t %= 300

answer[1] = t // 60
t %= 60

answer[2] = t // 10
t %= 10

if not t:
    print(*answer)
else:
    print(-1)