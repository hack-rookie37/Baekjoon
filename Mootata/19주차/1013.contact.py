import re

for t in range(int(input())):
    wave = input()
    
    if re.fullmatch('(100+1+|01)+', wave): # match는 앞 부분만 체크하기 때문에 문자열 전체를 체크하는 fullmatch 사용
        print("YES")
    else:
        print("NO")
