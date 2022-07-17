from sys import stdin


def sol(N):
    if liq[0] >= 0:
        print(liq[0], liq[1])
        return
    if liq[-1] <= 0:
        print(liq[-2], liq[-1])
        return

    answer = [float("inf"), (0, 0)]

    start, end = 0, N - 1

    while start < end:
        mix = liq[start] + liq[end]

        if mix == 0:
            print(liq[start], liq[end])
            return

        if answer[0] > abs(mix):
            answer[0] = abs(mix)
            answer[1] = (liq[start], liq[end])

        if mix < 0:
            start += 1

        else:
            end -= 1

    print(*answer[1])


N = int(stdin.readline())
liq = list(map(int, stdin.readline().split()))

sol(N)
