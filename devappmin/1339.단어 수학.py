import sys
from collections import defaultdict
from heapq import heappush, heappop

n = int(sys.stdin.readline())
words = sorted( [sys.stdin.readline().rstrip() for _ in range(n)], key=lambda a: -len(a))
sorted_list = []
exists = defaultdict(int)

for word in words:
    length = len(word)
    
    for idx in range(length):
        exists[word[idx]] += 10**(length - idx - 1)

ans = 0
val = 9

for word, size in exists.items():
    heappush(sorted_list, -size)

while sorted_list:
    item = heappop(sorted_list)
    ans += -1 * item * val
    val -= 1

print(ans)