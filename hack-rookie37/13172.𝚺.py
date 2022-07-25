import sys, math

input = sys.stdin.readline
Q = 1000000007


def modular(a, b):
    return (a % Q) * inverse(b, Q - 2) % Q


def inverse(n, exp):
    if exp == 1:
        return n

    if exp % 2 == 0:
        x = inverse(n, exp // 2)
        return x * x % Q
    else:
        return n * inverse(n, exp - 1) % Q


if __name__ == "__main__":
    M = int(input())

    sum = 0
    for _ in range(M):
        b, a = map(int, input().split())
        gcd = math.gcd(a, b)
        a //= gcd
        b //= gcd

        sum += (modular(a, b)) % Q

    print(sum % Q)
