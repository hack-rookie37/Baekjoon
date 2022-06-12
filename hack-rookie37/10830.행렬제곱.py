# for edit commit


def product(N, m1, m2):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000
    return result


def devide(N, B, matrix):
    if B == 1:
        return matrix
    elif B == 2:
        return product(N, matrix, matrix)
    else:
        tmp = devide(N, B // 2, matrix)

        if B % 2 == 0:
            return product(N, tmp, tmp)
        else:
            return product(N, product(N, tmp, tmp), matrix)


if __name__ == "__main__":

    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = devide(N, B, matrix)

    for row in result:
        print(*map(lambda x: x % 1000, row))
