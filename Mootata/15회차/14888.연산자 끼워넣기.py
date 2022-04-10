import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 수의 개수 n
numbers = list(map(int, input().split()))
operators = list(map(int, input().split())) # 순서대로 +, -, x, / 의 개수


def bfs():
    q = deque()
    q.append((numbers[0], 0, operators[0], operators[1], operators[2], operators[3]))
    max_answer = -float('inf')
    min_answer = float('inf')
    
    while q:
        num, count , plus, minus, multiply, division = q.popleft()
        
        if plus > 0:
            q.append((num + numbers[count + 1], count + 1, plus - 1, minus, multiply, division))
            
        if minus > 0:
            q.append((num - numbers[count + 1], count + 1, plus, minus - 1, multiply, division))
            
        if multiply > 0:
            q.append((num * numbers[count + 1], count + 1, plus, minus, multiply - 1, division))
            
        if division > 0:
            if num * numbers[count + 1] < 0: # 둘 중 하나만 음수일 때
                q.append((-(abs(num) // abs(numbers[count + 1])), count + 1, plus, minus, multiply, division - 1))
            else: # 둘 다 양수거나 음수일 때
                q.append(((num // numbers[count + 1]), count + 1, plus, minus, multiply, division - 1))

        if plus + minus + division + multiply == 0:
            max_answer = max(max_answer, num)
            min_answer = min(min_answer, num)

    return max_answer, min_answer

print(*bfs(),sep='\n')

# BFS를 통해 모든 경우의 수를 탐색함