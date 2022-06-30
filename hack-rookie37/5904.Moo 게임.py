N = int(input())


def moo(length, mid, N):
    x = (length - mid) // 2
    if N <= x:
        return moo(x, mid - 1, N)
    elif N > x + mid:
        return moo(x, mid - 1, N - x - mid)
    else:
        return "o" if N - x - 1 else "m"


length, k = 3, 0

while N > length:
    k += 1
    length = length * 2 + k + 3

print(moo(length, k + 3, N))
