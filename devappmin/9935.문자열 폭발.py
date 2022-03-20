import sys

string = sys.stdin.readline().strip()
explosion = list(sys.stdin.readline().strip())

s = []
weight = []

for idx in range(len(string)):
    s.append(string[idx])

    if len(explosion) == 1:
        if s[-1] == explosion[0]:
            s.pop()
        continue

    if len(s) == 1:
        weight.append(1 if string[idx] == explosion[0] else 0)
        continue

    if s[-1] == explosion[weight[-1]]:
        weight.append(weight[-1] + 1)
    elif s[-1] == explosion[0]:
        weight.append(1)
    else:
        weight.append(0)

    if weight[-1] == len(explosion):
        for _ in range(len(explosion)):
            weight.pop()
            s.pop()

print('FRULA' if not s else "".join(s))
