import sys

input = sys.stdin.readline

brackets = list(input().strip())
stack = []
answer = 0
temp = 1
last_bracket = ''

for bracket in brackets:
    if bracket == '(': # 여는 괄호들은 모두 스택에 담음
        stack.append(bracket)
        temp *= 2
    elif bracket == '[':
        stack.append(bracket)
        temp *= 3
    elif bracket == ')':
        if not stack or stack[-1] == '[': # 닫는 괄호인데 스택에 마지막으로 들어온 괄호와 모양이 다르거나
            answer = 0                    # 스택이 비어있을 때 (괄호의 짝이 맞지 않음)
            break
        
        if last_bracket == '(': # 직전의 괄호가 ( 일때
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        
        if last_bracket == '[':
            answer += temp
        
        stack.pop()
        temp //= 3
    
    last_bracket = bracket

if stack:
    print(0)
else:
    print(answer)