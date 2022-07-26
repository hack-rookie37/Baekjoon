import sys

DIV = 1000000007

n = int(sys.stdin.readline())

if n < 3:
    print(1)
    exit(0)

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    
    if n % 2:
        return matrix_mul(matrix_power(matrix, n - 1), matrix)
    
    return matrix_power(matrix_mul(matrix, matrix), n // 2)

def matrix_mul(ma, mb):
    temp_matrix = [[0] * len(mb[0]) for _ in range(2)]

    for y_idx in range(2):
        for x_idx in range(len(mb[0])):
            total = 0

            for k_idx in range(2):
                total += ma[y_idx][k_idx] * mb[k_idx][x_idx]
            
            temp_matrix[y_idx][x_idx] = total % DIV
    
    return temp_matrix


mul_value = [[1, 1], [1, 0]]
matrix = [[1], [1]]

print(matrix_mul(matrix_power(mul_value, n - 2), matrix)[0][0])