from collections import defaultdict

t = int(input())

def solution():
    c = int(input())
    d = defaultdict(list) 
    ans = 1
    
    for i in range(c):
        nam, typ = input().split()
        d[typ].append(nam)

    for k in d:
        ans *= len(d[k]) + 1
    
    ans -= 1
    print(ans)



for i in range(t):
    solution()


