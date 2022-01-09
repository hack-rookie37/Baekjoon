def coin_change(N):
    count = 0
    coins = [500, 100, 50, 10, 5, 1]
    c = 0

    while N > 0:
        i = coins[c]
        while i <= N:
            N -= i
            count += 1
        c += 1

    print(count)


N = int(input())  # 1 ~ 999
coin_change(1000 - N)
