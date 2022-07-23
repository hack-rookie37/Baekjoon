n = int(input())

nums = list(map(int, input().split()))
reversed_nums = list(reversed(nums))
lis = [1] * n # 가장 긴 증가하는 부분 수열
lds = [1] * n # 가장 긴 감소하는 부분 수열 (뒤로부터 역방향으로 증가하는 부분 수열)
answer = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            lis[i] = max(lis[i], lis[j] + 1) # 가장 긴 증가하는 부분 수열
        
        if reversed_nums[i] > reversed_nums[j]: # 가장 긴 감소하는 부분 수열 
            lds[i] = max(lds[i], lds[j] + 1)

for i in range(n):
    answer[i] = lis[i] + lds[n - 1 - i] - 1 # 각 위치의 가장 긴 증가 수열과 감소 수열의 길이를 더한 값

print(max(answer)) # 그 중 가장 큰 값이 정답.