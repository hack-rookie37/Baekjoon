text = input()
M = int(input())
left, right = list(text), list()

for _ in range(M):
    command, *c = input().split()

    if command == "L":
        if left:
            right.append(left.pop())
    elif command == "D":
        if right:
            left.append(right.pop())
    elif command == "B":
        if left:
            left.pop()
    else:
        left.append(*c)

right.reverse()
print("".join(left + right))
