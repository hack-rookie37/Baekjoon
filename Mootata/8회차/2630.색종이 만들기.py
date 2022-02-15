import sys

input = sys.stdin.readline

n = int(input()) # 한 변의 길이 n
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]

def cut_papers(x, y, n):
    current_color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if current_color != paper[i][j]:
                n //= 2
                cut_papers(x, y, n)
                cut_papers(x, y + n, n)
                cut_papers(x + n, y, n)
                cut_papers(x + n, y + n, n)
                # return
    if current_color == 0:
        answer[0] += 1
    elif current_color == 1:
        answer[1] += 1

cut_papers(0, 0, n)
print(*answer, sep = '\n')