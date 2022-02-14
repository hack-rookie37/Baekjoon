import sys

m = int(sys.stdin.readline()) # 수행해야 하는 연산의 수 m

s = set()

for i in range(m):
    cmd = sys.stdin.readline().strip().split()
    
    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = {i for i in range(1, 21)}
        else:
            s = set()
    
    else:
        command, value = cmd[0], int(cmd[1])
        if command == 'add':
            s.add(value)
        elif command == 'remove':
            s.discard(value)
        elif command == 'check':
            if value in s:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if value in s:
                s.discard(value)
            else:
                s.add(value)
