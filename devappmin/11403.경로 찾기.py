n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().replace("0", "999999999").split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for m in matrix:
    for i in m:
        print(0 if i == 999999999 else 1, end=" ")
    print()