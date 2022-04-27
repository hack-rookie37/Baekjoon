import sys
from collections import defaultdict
from heapq import heappush, heappop

n = int(sys.stdin.readline())
words = sorted( [sys.stdin.readline().rstrip() for _ in range(n)], key=lambda a: -len(a))
word_list = []
sorted_list = []

for word in words:
    length = len(word)
    
    for idx in range(length):
        word_list.append((10**(length - idx - 1), word[idx]))
    

exists = defaultdict(int)
ans = 0
val = 9

for size, word in word_list:
    exists[word] += -size

for _, size in exists.items():
    heappush(sorted_list, size)

while sorted_list:
    item = heappop(sorted_list)
    ans += -item * val
    val -= 1

print(ans)