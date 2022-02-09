import re

n = int(input()) # n개의 o로 이루어진 문자열  ex) n = 1, IOI   n = 2, IOIOI
m = int(input()) # 주어진 문자열의 길이 m
s = input()

iois = re.findall('I(?:OI)+', s)
count = 0

for i in iois:
    check = len(i) // 2 - n + 1 # IOI패턴을 가진 문자열의 길이를 2로 나눈 몫(O의 개수)에 n(찾는 패턴의 O의 개수)를 빼준 것에 + 1 해준 값이 
    if check > 0:               # 0보다 크다면 그 값을 답에 더해줌
        count += check
        
print(count)

# IOIOIOIOIOI 에 IOIOI가 4번 나오는데
# 이는 문자열의 길이 11을 2로 나눈 몫 5에서 찾는 패턴의 O의 개수 n = 2를 뺴주고, 거기에 1을 더해주면
# 마찬가지로 4가 나옴