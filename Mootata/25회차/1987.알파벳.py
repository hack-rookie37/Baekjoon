dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

r, c = map(int,input().split())
board = [list(input().strip()) for _ in  range(r)]

def bfs():
    q = set() # queue로 하니 메모리 초과
    q.add((0, 0, board[0][0])) # x, y, 지나온 알파벳
    answer = 0
    
    while q:
        x, y, alphabet = q.pop()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            
            if board[nx][ny] not in alphabet: # 다음 위치에 있는 알파벳을 지나온 적이 없다면
                q.add((nx, ny, alphabet + board[nx][ny]))
                answer = max(answer, len(alphabet))
    return answer + 1

print(bfs())