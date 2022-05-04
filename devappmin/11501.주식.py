import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    stocks = list(map(int, input().split()))

    base = stocks[-1]
    total = 0

    for idx in range(len(stocks) - 2, -1, -1):
        if stocks[idx] > base:
            base = stocks[idx]
        else:
            total += base - stocks[idx]

    print(total)
