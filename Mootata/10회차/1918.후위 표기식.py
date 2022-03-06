expression = list(input())
postfix = ''

stack = []

for i in expression:
    if i.isalpha():
        postfix += i
    else:
        if i == '(': # 여는 괄호는 일단 스택에 넣음
            stack.append(i) 
        elif i == '*' or i == '/': # *, /는 스택에 있는 *와 /를 모두 빼서 postfix에 넣고, 스택에 넣음
            while stack and (stack[-1] == '*' or stack [-1] =='/'):
                postfix += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-': # +, -는 스택에서 ( 가 아닌 수식들을 모두 꺼내서 postfix에 넣고, 스택에 넣음
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(i)
        elif i == ')': # ) 는 (가 나올 때까지 모든 수식을 postfix에 넣고, (도 꺼내서 버림
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

while stack: # 남아있는 수식 꺼내서 postfix에 넣기
    postfix += stack.pop()

print(postfix)