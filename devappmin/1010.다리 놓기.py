from math import factorial
import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    return factorial(m) // ( factorial(n) * factorial(m - n) )


loop_count = int(input())
for i in range(loop_count):
    print(solution())