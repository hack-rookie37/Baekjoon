import sys

n = int(input()) #N x N 크기의 종이
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = [0, 0, 0]

def recursive(x, y, n):
    current_color = paper[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != current_color:
                n //= 3
                recursive(x, y, n) # 1
                recursive(x, y + n, n) # 2
                recursive(x, y + (n * 2), n) # 3
                recursive(x + n, y, n) # 4
                recursive(x + n, y + n, n) # 5
                recursive(x + n, y + (n * 2), n) # 6
                recursive(x + (n * 2), y, n) # 7
                recursive(x + (n * 2), y + n, n) # 8
                recursive(x + (n * 2), y + (n * 2), n) # 9
                return
            
    if current_color == -1:
        count[0] += 1
    elif current_color == 0:
        count[1] += 1
    elif current_color == 1:
        count[2] += 1
    return
                
recursive(0, 0, n)
print(*count)      
              
              
                
# 1 2 3
# 4 5 6
# 7 8 9