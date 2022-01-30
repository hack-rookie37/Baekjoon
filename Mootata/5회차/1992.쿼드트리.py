n = int(input()) # 영상의 크기 N x N  N은 2의 제곱수

screen = [list(map(int, input())) for _ in range(n)]
answer = []

def recursive(x, y, n):
    current_color = screen[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if current_color != screen[i][j]:
                n //= 2
                answer.append('(')
                recursive(x, y, n) # 1
                recursive(x, y + n, n) # 2
                recursive(x + n, y, n) # 3
                recursive(x + n, y + n, n) # 4
                answer.append(')')
                return
    answer.append(current_color) # 위의 for문에서 나왔기 떄문에 범위 내의 색은 모두 같음

recursive(0, 0, n)
print(*answer, sep='')