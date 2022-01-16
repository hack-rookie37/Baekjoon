# @file 1927.최소힙.cpp
# @author @devappmin
# @brief 최소힙
# @version 0.1
# @date 2022-01-06
#
# @copyright Copyright (c) 2022 @devappmin

import sys
from collections import deque

loop = int(sys.stdin.readline().rstrip())

for i in range(loop):
    cmd = sys.stdin.readline().rstrip()
    size = int(sys.stdin.readline().rstrip())

    get = sys.stdin.readline().rstrip()
    get.replace('RR', '')
    arr = deque(map(int, get[1:-1].split(',')) if len(get) > 2 else [])

    err = False
    reverse = 0

    for cmd_char in cmd:
        if cmd_char == 'R':
            reverse += 1
            # arr = list(reversed(arr))
        elif cmd_char == 'D':
            if len(arr) < 1:
                err = True
                break

            if reverse % 2 == 0:
                # arr = arr[1:]
                arr.popleft()
            else:
                # arr = arr[:-1]
                arr.pop()

    if err:
        print("error")
    else:
        print("[", end="")
        print(*(list(arr)[:: -1 if reverse % 2 != 0 else 1]), sep=',', end="]\n")
