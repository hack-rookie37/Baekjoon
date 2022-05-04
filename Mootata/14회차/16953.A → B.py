import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

def bfs():
    global a
    q = deque()
    q.append((a, 1)) # a의 값, 연산 횟수
    
    while q:
        a, count = q.popleft()
        
        if a == b:
            return count
        
        if (a * 10) + 1 <= b: # a값의 맨 뒤에 1을 붙인 것이 b보다 작으면 큐에 넣음
            q.append(((a * 10) + 1, count + 1))
        if (a * 2) <= b: # a의 2배 한 값이 b보다 작으면 큐에 넣음
            q.append((a * 2, count + 1))
    return -1

print(bfs())