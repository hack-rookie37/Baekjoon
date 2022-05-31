import sys

n = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
alkalis = sorted([x for x in solutions if x < 0])
acids = sorted([x for x in solutions if x > 0], key=lambda a: -a)

alkali, acid = 0, 0

if not alkalis:
    solutions = sorted(solutions)
    print(solutions[0], solutions[1])
    exit()

if not acids:
    solutions = sorted(solutions)[::-1]
    print(solutions[1], solutions[0])
    exit()

abs_value = alkalis[0] + acids[0]
position = [0, 0]

while alkali < len(alkalis) or acid < len(acids):

    if acid < len(acids) - 1 and alkali < len(alkalis) - 1 and abs(alkalis[alkali + 1] + acids[acid]) < abs(alkalis[alkali] + acids[acid + 1]):
        alkali += 1
    elif acid < len(acids) - 1:
        acid += 1
    else:
        break

    if abs(alkalis[alkali] + acids[acid]) < abs(abs_value):
        abs_value = alkalis[alkali] + acids[acid]
        position = [alkali, acid]

print(alkalis[position[0]], acids[position[1]])