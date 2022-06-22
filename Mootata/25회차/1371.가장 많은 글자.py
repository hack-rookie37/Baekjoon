import sys
from collections import defaultdict

s = sys.stdin.read()
dic = defaultdict(str)
for i in s:
    dic[i] += 1

print(max(dic))