import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    
    if a == 1 or a == 5 or a == 6:
        print(a)
        continue
    
    result_list = []
    temp = 1
    for _ in range(b):
        temp *= a 
        temp %= 10 
        if temp in result_list:
            break 
        result_list.append(temp)
    
    result = result_list[b % len(result_list) - 1]
    if result == 0: 
        print(10) 
    else: 
        print(result)
