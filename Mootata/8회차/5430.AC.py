import sys
from collections import deque

input = sys.stdin.readline

for t in range(int(input())):
    cmds = list(input().rstrip())
    n = int(input())
    is_reverse = False
    is_error = False
    
    if n != 0:
        q = deque()
        for i in list(input().rstrip()[1:-1].split(',')):
            q.append(i)
    else:
        _ = input()
        q = deque()

    for cmd in cmds:
        if cmd == 'R':
            if not is_reverse:
                is_reverse = True
            else:
                is_reverse = False
        else:
            if not q:
                is_error = True
                break
            else:
                if not is_reverse:
                    q.popleft()
                else:
                    q.pop()
    if is_error:
        print('error')
    elif not is_reverse:
        print('[' + ','.join(q) + ']')
    else:
        print('[' + ','.join(reversed(q)) + ']')