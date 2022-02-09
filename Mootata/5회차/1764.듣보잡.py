import sys

n, m = map(int, input().split()) # 들어본 적 없는 사람 수 n, 본 적 없는 사람 수 m

never_heard = {}
never_seen = []
answer = []

for i in range(n):
    never_heard[sys.stdin.readline()] = i
    
for i in range(m):
    never_seen.append(sys.stdin.readline())
    
for i in range(m):
    if never_seen[i] in never_heard:
        answer.append(never_seen[i])
        
answer.sort()
print(len(answer))  
print(*answer, sep='')