from collections import deque


def to_list(e):
    if isinstance(e, deque):
        return list(e)
    return e


T = int(input())
output = []
for _ in range(T):
    p = input()  # R: reverse, D: delete
    n = int(input())  # len(x) <= 100,000
    x = deque(input()[1:-1].split(","))
    direction = 1

    if p.count("D") > n:
        output.append("error")
        continue

    for func in p:
        if func == "R":
            direction *= -1
        else:
            if x:
                if direction > 0:
                    x.popleft()
                else:
                    x.pop()

    if direction < 0:
        x.reverse()
    output.append(x)

output = list(map(to_list, output))

for e in output:
    if isinstance(e, list):
        n = ",".join(e)
        print("".join(("[", n, "]")))
    else:
        print(e)
