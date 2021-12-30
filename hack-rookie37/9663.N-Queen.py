def n_queen(r, N):
    global result, depth, o_result
    if r == N:
        result += 1
        return

    else:
        K = N
        if depth == 0:
            if N % 2 == 0:
                K = N//2
            else:
                K = N//2 + 1
        for i in range(K):
            if N % 2 == 1 and i == K-1 and depth == 0:
                o_result = result
            matrix[r] = i
            for j in range(r):
                if matrix[j] == matrix[r] or (matrix[r] - r) == (matrix[j] - j) or (matrix[r] + r) == (matrix[j] + j):
                    break
            else:
                depth += 1
                n_queen(r+1, N)
                depth -= 1


if __name__ == '__main__':
    N = int(input())

    result = 0
    o_result = 0
    depth = 0
    matrix = [0] * N

    n_queen(0, N)

    if N % 2 == 0:
        result *= 2
    else:
        result = o_result*2 + (result - o_result)

    print(result)
