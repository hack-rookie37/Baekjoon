import sys

n, m = map(int, sys.stdin.readline().split())
min_box, min_piece = 1001, 1001

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    min_piece = min(min_piece, b)
    min_box = min(min_box, a, min_piece * 6)

print(min(n // 6 * min_box + n % 6 * min_piece, (n // 6 + 1) * min_box))