import sys
import re

s = sys.stdin.readline().rstrip()
m = re.fullmatch(r'((pi)*(ka)*(chu)*)*', s)
print("YES" if m else "NO")