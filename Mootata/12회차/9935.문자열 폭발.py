import sys

input = sys.stdin.readline

string = list(input().rstrip())
bombs = list(input().rstrip())
stack = []

for char in string:
    stack.append(char) # 스택에 문자 하나씩 넣음
    
    # 만약 방금 들어간 문자가 폭탄 문자열의 끝부분과 같다면, 폭탄 문자열의 길이만큼
    # 스택의 뒷부분에서 폭탄 문자열과 같은지 확인함.
    if stack[-1] == bombs[-1] and ''.join(stack[-len(bombs):]) == ''.join(bombs):
        for _ in range(len(bombs)): # 같다면 스택에서 폭탄 문자열의 길이만큼 pop
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')