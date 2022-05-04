import sys
from collections import deque

input_list = ['(', *list(sys.stdin.readline().rstrip()), ')']
stack = deque()

for item in input_list:
    if item.isalpha():
        print(item, end='')
        continue

    if item == ')':
        pop = stack.pop()

        while stack and pop != '(':
            print(pop, end='')
            pop = stack.pop()
        
        continue
    
    if item == '+' or item == '-':
            while stack and stack[-1] != '(':
                pop = stack.pop()
                if pop == '(':
                    break
                print(pop, end='')
    elif item == '*' or item == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')

    stack.append(item)