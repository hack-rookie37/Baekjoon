import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
target_matrix = [list(map(int, input().strip())) for _ in range(n)]
count = 0
success = True

for i in range(0, n - 2): # 범위 벗어나지 않게 -2
    for j in range(0, m - 2):
        if matrix[i][j] != target_matrix[i][j]:
            count += 1
            
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    matrix[k][l] = 1 - matrix[k][l]

for i in range(n):
    if matrix[i] != target_matrix[i]:
        print(-1)
        success = False
        break

if success:
    print(count)

# 3 x 3씩 특정한 위치를 바꿔서 만드는게 아니라
# 그냥 (0, 0)부터 차례대로 지나가면서 해당 위치의 값이
# 다를 때마다 바꿔준다고 생각하면 더 쉬운듯