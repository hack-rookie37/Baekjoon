t = int(input()) # 테스트 케이스 수 t

for i in range(t):
    m, n, x, y = map(int, input().split())
    is_find = False
    
    while x <= m * n:
        if (x - y) % n == 0: # x를 n으로 나눈 값과 y를 n으로 나눈 값이 같을 때가 정답
            print(x)
            is_find = True
            break
        x += m
    
    if not is_find:
        print(-1)
        
# x와 y를 1씩 증가시키면 시간초과

# ex) x = 3, y = 9 인 달력의 해는 x가 3인 해인 3년, 13년, 23년, 33년과
#                                y가 9인 해인 9년, 21년, 33년 중
# x와 y가 같은 33년이 정답임. 