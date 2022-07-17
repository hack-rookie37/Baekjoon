import re

p = re.compile("^[ABCDEF]?A+F+C+[ABCDEF]?$")
T = int(input())

for _ in range(T):
    S = input()

    if p.match(S):
        print("Infected!")
    else:
        print("Good")
