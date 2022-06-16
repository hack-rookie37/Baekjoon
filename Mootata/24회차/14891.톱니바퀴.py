from collections import deque

gears = [deque(map(int, input().strip())) for _ in range(4)]
answer = 0

for k in range(int(input())):
    n, d = map(int, input().split()) # 회전 시킨 톱니의 번호 N, 방향 D
    n -= 1 # 인덱스는 0부터 시작
    
    temp2, temp6, tempd = gears[n][2], gears[n][6], d
    
    gears[n].rotate(d)
    
    for i in range(n - 1, -1, -1): # 회전한 톱니 왼쪽
        if gears[i][2] != temp6:
            temp6 = gears[i][6]
            tempd *= -1 # 반대방향으로 회전
            gears[i].rotate(tempd)
            
        else:
            break
    
    tempd = d
    for i in range(n + 1, 4): # 오른쪽
        if gears[i][6] != temp2:
            temp2 = gears[i][2]
            tempd *= -1 # 반대방향으로 회전
            gears[i].rotate(tempd)
        else:
            break

for i in range(4):
    if gears[i][0] == 1:
        answer += 2 ** i

print(answer)