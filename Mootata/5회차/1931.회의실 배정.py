import sys

n = int(input()) # 회의의 수 n
time = []
last = 0
count = 1

for _ in range(n):
    time.append(tuple(map(int, (sys.stdin.readline().split()))))
    
time.sort(key = lambda x: (x[1], x[0])) # 끝나는 시간을 기준으로 정렬하고 끝나는 시간이 같은 것들은 시작 시간을 기준으로 정렬
    
for i in range(1, n):
    if time[last][1] <= time[i][0]: # 이전에 했던 회의의 끝나는 시간보다 시작 시간이 늦거나 같다면 배정 가능
        count += 1
        last = i
    
print(count)