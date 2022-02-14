import sys

n, m = map(int, sys.stdin.readline().split()) # 저장된 사이트 주소의 수 n, 비밀번호를 찾으려는 사이트의 주소 수 m

passwords = {}

for i in range(n):
    address, pw = sys.stdin.readline().split()
    passwords[address] = pw # 사이트 주소를 키로가지는 값을 딕셔너리에 넣어줌
    
for j in range(m):
    find_pw = sys.stdin.readline().rstrip() # 개행문자 제거 해줘야함
    print(passwords[find_pw])