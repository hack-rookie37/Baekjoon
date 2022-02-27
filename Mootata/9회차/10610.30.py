import sys
from itertools import permutations

input = sys.stdin.readline

n = list(input().rstrip()) # 양수 n
digit = len(n)
answer = 0

def sol1():
    permus = list(permutations(n, digit))
    permus.sort(reverse = True)
    is_find = False
    
    for num in permus:
        check = int(''.join(num))
        if check % 30 == 0:
            is_find = True
            return check
        if not is_find:
            return -1

def sol2():
    n.sort(reverse = True)
    sum = 0
    
    if '0' not in n:
        return -1
    
    for i in n:
        sum += int(i)
        
    if sum % 3 != 0:
        return -1
    
    return ''.join(n)
        

print(sol2())

# 3의 배수 판정법
# 모든 자리의 수를 더한 것이 3의 배수이면 그 수는 3의 배수임.

# 30의 배수는 모든 자리의 수를 더해서 3의 배수가 되고, 맨 끝자리가 0이면 됨