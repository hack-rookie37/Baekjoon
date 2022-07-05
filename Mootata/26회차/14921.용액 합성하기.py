n = int(input())
sol = list(map(int, input().split()))
answer = float('inf')
left, right = 0, n - 1

while left < right:
    s = sol[left] + sol[right]
    if abs(answer) > abs(s):
        answer = s
    
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        left += 1
        right -= 1

print(answer)