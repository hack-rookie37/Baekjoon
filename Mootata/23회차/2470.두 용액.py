n = int(input()) # 용액의 수 N
sol = sorted(list(map(int, input().split())))
start, end = 0, n - 1
answer = 2000000001

while start < end:
    if answer > abs(sol[start] + sol[end]): # 두 값을 더한 것이 기존의 값보다 0에 가깝다면
        answer = abs(sol[start] + sol[end])
        sols = [sol[start], sol[end]]
    
    if sol[start] + sol[end] < 0: # 두 값의 합이 0보다 작으면 start를 밀어서 0에 가깝게
        start += 1
    else: # 0보다 크면 end를 당겨서 0에 가깝게
        end -= 1

print(*sols)