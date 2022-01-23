from sys import stdin
from array import array

input = stdin.readline


def is_prime(n):
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":

    answer = []

    while True:
        N = int(input())
        if N == 0:
            break

        for i in range(3, (N // 2) + 1, 2):
            if is_prime(i) and is_prime(N - i):
                answer.append(f"{N} = {i} + {N-i}")
                break
        else:
            print("Goldbach's conjecture is wrong.")

    print(*answer, sep="\n")
