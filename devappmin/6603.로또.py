import sys
from itertools import combinations

lottos = []

input_value = sys.stdin.readline().rstrip()

while input_value != '0':
    lottos.append(list(map(int, input_value.split())))
    input_value = sys.stdin.readline().rstrip()

for lotto in lottos:
    k = lotto[0]
    s = lotto[1:]
    for numbers in combinations(s, 6):
        print(*numbers)

    print()
