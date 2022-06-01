import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(n)]

left, right = 0, k - 1
answer = 0

while left != n:
    right = left + k

    contain = set(sushi[x % n] for x in range(left, right))
    
    values = len(contain)
    if c not in contain:
        values += 1 

    answer = max(answer, values)
    left += 1

print(answer)