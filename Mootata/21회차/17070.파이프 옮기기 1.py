from collections import deque

dx, dy = [1, 0, 1], [0, 1, 1] # 아래, 오른쪽, 대각선 아래

n = int(input()) # n x n
house = [list(map(int, input().split())) for _ in range(n)]
count = 0

def dfs(state, x, y):
    global count
    
    if x == n - 1 and y == n - 1: # 파이프의 끝 부분이 (n - 1, n - 1)에 닿으면 count +1
        count += 1
        return
    
    if state == 'h' or state == 'd': # 가로 또는 대각선일 때
        if y + 1 < n: # 오른쪽으로만 움직일 수 있음
            if house[x][y + 1] == 0:
                dfs('h', x, y + 1)
    if state == 'v' or state == 'd': # 세로 또는 대각선일 때
        if x + 1 < n: # 아래쪽으로만 움직일 수 있음
            if house[x + 1][y] == 0:
                dfs('v', x + 1, y)
                
    # 대각선일 떄는 가로 세로 대각선 모든 형태로 이동 가능
    if x + 1 < n and y + 1 < n: # 대각선 아래로만 이동할 수 있음
        if house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
            dfs('d', x + 1, y + 1)

dfs('h', 0, 1)
print(count)