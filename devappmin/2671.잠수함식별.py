import re
import sys

s = sys.stdin.readline().rstrip()
m = re.fullmatch("(100+1+|(01))+", s)
print("SUBMARINE" if m else "NOISE")