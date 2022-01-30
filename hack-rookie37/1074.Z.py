def dq(N, r, c):
    ans = 0

    while N != 0:

        N -= 1

        x = 2 ** N

        # 1사분면
        if r < x and c < x:
            # ans += x ** 2 * 0
            continue

        # 2사분면
        elif r < x and c >= x:
            ans += x ** 2 * 1
            c -= x

        # 3사분면
        elif r >= x and c < x:
            ans += x ** 2 * 2
            r -= x

        # 4사분면
        else:
            ans += x ** 2 * 3
            r -= x
            c -= x

    return ans


def recursion(N, r, c):
    if N == 0:
        return 0

    return 2 * (r % 2) + (c % 2) + 4 * recursion(N - 1, r // 2, c // 2)


if __name__ == "__main__":
    N, r, c = map(int, input().split())

    print(dq(N, r, c))
    print(recursion(N, r, c))
