n = int(input()) # 우유 가게의 수 N
stores = list(map(int,input().split()))

answer = 0

for i in range(n):
    if stores[i] == answer % 3:
        answer += 1

print(answer)