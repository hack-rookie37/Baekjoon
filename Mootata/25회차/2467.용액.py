n = int(input()) # 전체 용액의 수 N
sol = list(map(int, input().split()))
answer = [sol[0], sol[n - 1]]
left, right = 0, n - 1

while left < right:
    if abs(sol[left] + sol[right]) < abs(answer[0] + answer[1]): # 기존의 answer보다 더 0에 가까우면 초기화
        answer = [sol[left], sol[right]]
    if sol[left] + sol[right] < 0: # 두 용액의 합이 0보다 작으면 left 오른쪽으로 이동
        left += 1
    else: # 0보다 크면 right 왼쪽으로 이동
        right -= 1

print(*answer)