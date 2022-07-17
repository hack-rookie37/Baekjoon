def sol(N, liq):
    if liq[0] >= 0:
        return liq[0] + liq[1]

    elif liq[-1] <= 0:
        return liq[-1] + liq[-2]

    left, right = 0, len(liq) - 1
    answer = float("inf")

    while left < right:
        x = liq[left] + liq[right]

        if x == 0:
            return 0
        elif x > 0:
            right -= 1
        else:
            left += 1

        if answer > abs(x):
            answer = x
            
    return answer


N = int(input())
liq = list(map(int, input().split()))

print(sol(N, liq))
