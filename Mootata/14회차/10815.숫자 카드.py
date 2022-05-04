import sys

input = sys.stdin.readline

n = int(input()) # 숫자 카드의 개수
cards = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))
answer = []

for num in check:
    start = 0
    end = len(cards) - 1
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        
        if num == cards[mid]:
            ans = 1
            break
        elif num > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1
    answer.append(ans)

print(*answer)