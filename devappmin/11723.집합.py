import sys

s = set()
loop = int(sys.stdin.readline())

for i in range(loop):
    cmd = list(sys.stdin.readline().split())

    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
    
    if cmd[0] == 'add':
        s.add(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in s:
            s.discard(cmd[1])
    elif cmd[0] == 'check':
        print(1 if cmd[1] in s else 0)
    elif cmd[0] == 'toggle':
        if cmd[1] in s:
            s.discard(cmd[1])
        else:
            s.add(cmd[1])
    elif cmd[0] == 'all':
        s = {x for x in range(1, 21)}
    elif cmd[0] == 'empty':
        s = set()