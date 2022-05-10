n, b = map(int, input().split()) # 행렬의 크기 N x N, 주어진 행렬의 B제곱
matrix = [list(map(int, input().split())) for _ in range(n)]

def multiply(m1, m2): # 행렬의 곱셈
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000
    
    return result

def divide(b, matrix): # 분할 정복
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        print(b)
        return matrix
    else: 
        if b % 2 == 0: # A^4 = A^2 * A^2
            temp = divide(b // 2, matrix)
            print(b)
            return multiply(temp, temp)
        else: # A^5 = A^2 * A^2 * A^1
            temp = divide(b - 1, matrix)
            print(b)
            return multiply(matrix, temp)

answer = divide(b, matrix)

for i in answer:
    print(*i)