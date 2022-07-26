import sys

X = 1000000007

def mul(b, t):
    if t == 1:
        return b % X
    
    if not t % 2:
        temp = mul(b, t // 2)
        return temp ** 2 % X
    
    return b * mul(b, t - 1) % X

division = lambda a, b: b * mul(a, X - 2) % X

answer = 0
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n, s = map(int, sys.stdin.readline().split())
    answer += division(n, s)
    answer %= X

print(answer)
