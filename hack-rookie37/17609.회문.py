def palin(tc, flag):
    left = 0
    right = len(tc) - 1

    while left < right:
        if tc[left] == tc[right]:
            left += 1
            right -= 1
            continue
        else:
            if flag >= 1:
                return 2

            if palin(tc[left:right], 1) == 1:
                return 1
            elif palin(tc[left + 1 : right + 1], 1) == 1:
                return 1
            else:
                return 2

    return flag


if __name__ == "__main__":
    N = int(input())
    answer = []
    for _ in range(N):
        tc = input()

        print(palin(tc, 0))
