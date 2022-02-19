import sys
from collections import deque

input = sys.stdin.readline

for t in range(int(input())):
    cmds = list(input().rstrip())
    n = int(input())
    is_reverse = False # reverse는 체크만 하다가 마지막에 한번만 뒤집어줌
    is_error = False # deque이 비어있을 때 D 명령어가 들어오는지 확인
    
    if n != 0: # 배열에 들어있는 수의 개수가 0이 아닐 때
        q = deque()
        for i in list(input().rstrip()[1:-1].split(',')):
            q.append(i)
    else: # 배열에 들어있는 수의 개수가 0일 때
        _ = input() # 배열에 수가 들어있지 않아도 '[]'는 입력되기 때문에 받아줌
        q = deque() # deque는 선언만 함

    for cmd in cmds:
        if cmd == 'R': # reverse는 체크만 함
            if not is_reverse:
                is_reverse = True
            else:
                is_reverse = False
        else: # D가 입력되었고,
            if not q: # deque가 비어있다면
                is_error = True
                break
            else: # deque가 비어있지 않고,
                if not is_reverse: # reverse 명령어가 입력된 적이 없거나 짝수번 입력되었다면,
                    q.popleft() # 맨 앞에서 값을 제거
                else: # reverse 명령어가 홀수번 입력되었다면,
                    q.pop() # 맨 뒤에서 값을 제거
    if is_error:
        print('error')
    elif not is_reverse:
        print('[' + ','.join(q) + ']')
    else:
        print('[' + ','.join(reversed(q)) + ']')