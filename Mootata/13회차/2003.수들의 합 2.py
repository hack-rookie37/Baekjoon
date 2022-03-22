import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # n개의 수 , 합 m
numbers = list(map(int, input().split()))
left, right = 0, 1
count = 0

while left <= right and right <= n:
    sum_num = sum(numbers[left:right])
    
    if sum_num == m: # 범위내의 값을 더한 것이 찾고 있는 m 이라면 포인터 둘 다 오른쪽으로 한칸씩 이동
        count += 1
        right += 1
        left += 1
    elif sum_num > m: # 범위내의 값을 더한 것이 m보다 크다면 왼쪽 포인터 한칸 이동
        left += 1
    else: # 범위내의 값을 더한 것이 m보다 작다면 오른쪽 포인터 한칸 이동
        right += 1
print(count)