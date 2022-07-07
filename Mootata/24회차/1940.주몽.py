n = int(input()) # 재료의 개수 N
m = int(input()) # 갑옷을 만드는데 필요한 수 M
ingr = sorted(list(map(int, input().split())))
answer = 0
left, right = 0, n - 1

while left < right:
    if ingr[left] + ingr[right] < m:
        left += 1
    elif ingr[left] + ingr[right] > m:
        right -= 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)