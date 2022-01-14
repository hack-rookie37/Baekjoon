import sys

stack_1 = list(sys.stdin.readline().rstrip())
stack_2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if stack_1:
            stack_2.append(stack_1.pop())
    elif command[0] == 'D':
        if stack_2:
            stack_1.append(stack_2.pop())
    elif command[0] == 'B':
        if stack_1:
            stack_1.pop()
    else:
        stack_1.append(command[1])
        
stack_1.extend(reversed(stack_2)) # 두 스택을 합쳐줌
print(''.join(stack_1))