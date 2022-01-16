n = int(input()) # 지도의 크기
town = [list(map(int, input())) for _ in range(n)] # n개의 값을 n줄 받아서 리스트에 저장
visited = [[False] * (n) for _ in range(n)] # 방문한 적 있는지 체크
answer = [] # 단지별 집의 수

d_col, d_row = [-1, 1, 0, 0], [0, 0, -1, 1] # 위, 아래, 좌, 우 확인용 

def dfs(col, row):
    global count
    count += 1
    visited[col][row] = True
    
    for i in range(4):
        n_col, n_row = col + d_col[i], row + d_row[i]
        
        if 0 <= n_col < n and 0 <= n_row < n:
            if town[n_col][n_row] == 1 and visited[n_col][n_row] == False:
                dfs(n_col, n_row)
                
for col in range(n):
    for row in range(n):
        if town[col][row] == 1 and visited[col][row] == False:
            count = 0 # 집의 수
            dfs(col, row)
            answer.append(count)
            
print(len(answer))
answer.sort()
print(*answer, sep = '\n')
