n, m = map(int, input().split()) # 종이의 세로크기 n, 가로크기 m
paper = [list(map(int, input().split())) for _ in range(n)]

shapes = [
    [[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]], # ㅣ
    
    [[0, 0], [0, 1], [1, 0], [1, 1]], # ㅁ
    
    [[0, 0], [0, 1], [0, 2], [-1, 2]], [[0, 0], [1, 0], [1, 1], [1, 2]], # ㄱ
    [[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]], [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [1, 0], [2, 0], [2, 1]], 
    
    [[0, 0], [0, 1], [1, 1], [1, 2]], [[0, 0], [0, 1], [-1, 1], [-1, 2]], # z 
    [[0, 0], [1, 0], [1, -1], [2, -1]], [[0, 0], [1, 0], [1, 1], [2, 1]], 
    
    [[0, 0], [1, 0], [2, 0], [1, 1]], [[0, 0], [1, 0], [2, 0], [1, -1]], # ㅗ
    [[0, 0], [0, 1], [0, 2], [-1, 1]], [[0, 0], [0, 1], [0, 2], [1, 1]]
]

answer = 0

for i in range(n):
    for j in range(m):
        for shape in shapes:
            count = 0
            for s in shape:
                if 0 <= i + s[0] < n and 0 <= j + s[1]< m:
                    count += paper[i + s[0]][j + s[1]]
            answer = max(answer, count)

print(answer)

# 모든 칸을 돌면서 해당 칸을 기준으로 shapes에 있는 값들을 더해서 테트로미노를 만들고 범위를 벗어나지 않는다면
# 그 값들을 더하여 count에 넣고, answer와 비교해서 더 큰 값을 answer에 넣어줌