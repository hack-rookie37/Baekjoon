import re
import sys

n = int(sys.stdin.readline())
p = sys.stdin.readline().rstrip().split("*")
pattern = p[0] + '[a-z]*' + p[1]
r = re.compile(pattern)

for _ in range(n):
    m = r.fullmatch(sys.stdin.readline().rstrip())
    print("DA" if m else "NE")