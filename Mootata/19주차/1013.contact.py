import re

for t in range(int(input())):
    wave = input().replace('\n', '')
    pattern = re.compile('(100+1+|01)+')
    
    if pattern.fullmatch(wave):
        print("YES")
    else:
        print("NO")
