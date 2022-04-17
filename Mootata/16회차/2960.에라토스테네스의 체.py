import sys

input = sys.stdin.readline

n, k = map(int, input().split()) # N보다 작거나 같은 소수를 지울 때 k번째로 지워지는 수

primes = [True] * (n + 1)

def prime_check():
    count = 0
    
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if primes[j]:
                primes[j] = False
                count += 1
                if count == k:
                    return j

print(prime_check())