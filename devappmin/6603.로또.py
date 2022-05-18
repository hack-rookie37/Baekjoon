import sys
from itertools import combinations

lottos = []

input_value = sys.stdin.readline().rstrip()
while input_value != '0':
    lottos.append(list(map(int, input_value.split()))[1:])
    input_value = sys.stdin.readline().rstrip()

for lotto in lottos:
    for numbers in combinations(lotto, 6):
        print(*numbers)
    print()