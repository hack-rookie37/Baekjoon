n = int(input())

nums = list(map(int, input().split()))
reversed_nums = list(reversed(nums))
lis = [1] * n
lds = [1] * n
answer = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            lis[i] = max(lis[i], lis[j] + 1)
        
        if reversed_nums[i] > reversed_nums[j]:
            lds[i] = max(lds[i], lds[j] + 1)

for i in range(n):
    answer[i] = lis[i] + lds[n - 1 - i] - 1

print(max(answer))