import sys

input = sys.stdin.readline

for t in range(3):
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    
    if sum(numbers) > 0:
        print('+')
    elif sum(numbers) < 0:
        print('-')
    else:
        print('0')