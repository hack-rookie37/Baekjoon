n = int(input())
m = 1000000007

def mul(mat1, mat2): # 행렬 곱셈
    answer = []
    
    for i in range(len(mat1)):
        answer.append([])
        for j in range(len(mat2[0])):
            temp = 0
            for k in range(len(mat1[0])):
                temp += mat1[i][k] * mat2[k][j]
            answer[i].append(temp % m)
    return answer

def power(mat, p): # 행렬 거듭제곱
    if p == 1:
        return mat
    else:
        temp = power(mat, p // 2)
        
        if p % 2 == 0:
            return mul(temp, temp)
        else:
            return mul(mul(temp, temp), mat)

print(power([[1, 1], [1, 0]], n)[0][1])