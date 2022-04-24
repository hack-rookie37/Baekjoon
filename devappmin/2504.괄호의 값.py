import sys
from collections import deque

brackets = list(sys.stdin.readline().rstrip())
s = deque()

ans = True

for bracket in brackets:
    
    if bracket == '(' or bracket == '[':
        s.append(bracket)
        continue
    

    if bracket == ']':
        if not s:
            ans = False
            break
        
        if type(s[-1]) == int:
            if len(s) == 1 or s[-2] != '[':
                ans = False
                break
            else:
                n = s.pop()
                s.pop()
                s.append(n * 3)
        elif s[-1] == '[':
            s.pop()
            s.append(3)
        else:
            ans = False
            break

    elif bracket == ')':
        if not s:
            ans = False
            break
        
        if type(s[-1]) == int:
            if len(s) == 1 or s[-2] != '(':
                ans = False
                break
            else:
                n = s.pop()
                s.pop()
                s.append(n * 2)
        elif s[-1] == '(':
            s.pop()
            s.append(2)
        else:
            ans = False
            break
    while len(s) >= 2:
        if type(s[-1]) == int and type(s[-2]) == int:
            a, b = s.pop(), s.pop()
            s.append(a + b)
        else:
            break
i = 0
if s:
    i = s.pop()

print(0 if not ans or s or type(i) != int else i)