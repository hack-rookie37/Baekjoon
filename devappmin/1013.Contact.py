import sys
import re

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    s = sys.stdin.readline().rstrip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(s)
    print("YES" if m else "NO")