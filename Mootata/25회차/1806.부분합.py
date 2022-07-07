import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 길이 N짜리 수열에서 연속된 수들의 부분합 중 그 합이 S 이상
nums = list(map(int, input().split()))
answer = float('inf')
left, right = 0, 0
s = nums[0]

while left < n and right < n:
    if left > right:
        left = right
    if s >= m: # 부분합이 m 이상일 때 
        answer = min(answer, right - left + 1)
        s -= nums[left]
        left += 1 # left 한칸 당김
    else: # 부분합이 m보다 작을 때
        right += 1 # right 한칸 밈
        if right < n:
            s += nums[right]

if answer == float('inf'):
    print(0)
else:
    print(answer)

