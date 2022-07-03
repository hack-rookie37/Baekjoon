import sys

n = int(sys.stdin.readline())

def moo(acc, cur, n):
    prev = (acc - cur)//2
    if n <= prev:
        return moo(prev, cur - 1, n)
    elif n > prev + cur:
        return moo(prev, cur - 1, n - prev - cur)
    else:
        return "o" if n - prev - 1 else "m"

acc, num = 3, 0
while n > acc:
    num += 1
    acc = acc * 2 + num + 3

print(moo(acc, num + 3, n))

# Moo(n) = Moo(n-1) + "m" + "o"*(n+2) + Moo(n-1)
# moo길이, 가운데 길이, n