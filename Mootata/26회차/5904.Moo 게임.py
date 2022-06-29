n = int(input())

def moo(acc, cur, n):
    prev = (acc - cur) // 2
    if n <= prev:
        return moo(prev, cur - 1, n)
    elif n > prev + cur:
        return moo(prev, cur - 1, n - prev - cur)
    else:
        if n - prev - 1:
            return "o"
        else:
            return "m"

acc, m = 3, 0
while n > acc:
    m += 1
    acc = acc * 2 + m + 3

print(moo(acc, m + 3, n)) # moo(n)의 길이, 가운데 moo의 길이, n