def fibo(N):
    f = [0, 1] + [None] * 19

    for i in range(2, N + 1):
        f[i] = f[i - 1] + f[i - 2]

    print(f[N])


fibo(int(input()))
