import re

for t in range(int(input())):
    wave = input()
    
    if re.fullmatch('(100+1+|01)+', wave): # match는 앞부분에서 정규식에 매치되는 
        print("YES")
    else:
        print("NO")
