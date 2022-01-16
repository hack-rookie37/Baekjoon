def find_house(matrix, i, j):
    count = 1
    matrix[i][j] = 0
    for k in range(4):
        x, y = i + DX[k], j + DY[k]
        if 0 <= x < N and 0 <= y < N:
            if matrix[x][y] == 1:
                count += find_house(matrix, x, y)
    return count


if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    # 0: right, 1: down, 2: left, 3: up
    DX = (1, 0, -1, 0)
    DY = (0, -1, 0, 1)

    complex = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                complex.append(find_house(matrix, i, j))

    complex.sort()
    print(len(complex))
    print(*complex, sep="\n")
