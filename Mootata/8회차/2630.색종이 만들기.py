n = int(input()) # 한 변의 길이 n
paper = [list(map(int, input().split())) for _ in range(n)]

def cut_papers(x, y, n):
    current_color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if current_color == paper[x][y]:
                