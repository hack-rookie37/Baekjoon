import sys
import re

result = []

for i in range(int(sys.stdin.readline())): # 테스트케이스 수 만큼 반복
    command = list(sys.stdin.readline().rstrip()) # 명령어
    n = int(sys.stdin.readline()) # 배열에 들어있는 수의 개수
    stack_1 = [int(i) for i in re.findall('\d+', sys.stdin.readline())]
    stack_2 = []
    for j in range(len(command)):
        if command[j] == 'R':
            if stack_1:
                for _ in range(len(stack_1)):
                    stack_2.append(stack_1.pop())
            elif stack_2:
                for _ in range(len(stack_2)):
                    stack_1.append(stack_2.pop())
        if command[j] == 'D':
            if not stack_1 and not stack_2:
                result.append('error')
            elif stack_1:
                stack_1.pop(0)
            elif stack_2:
                stack_2.pop(0)

    if stack_1:
        result.append(stack_1)
    elif stack_2:
        result.append(stack_2)
            
print(*result, sep='\n')