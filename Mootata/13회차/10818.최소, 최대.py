import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))