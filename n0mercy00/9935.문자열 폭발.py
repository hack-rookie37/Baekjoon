from sys import stdin
string=input()
boom = input()
lastchar = boom[-1]
length = len(boom)
stack = []

for char in string:
    #입력받은 문자열을 한글자씩 스택에 추가
    stack.append(char)
    
    #입력받는 문자가 == boom 단어의 마지막 단어와 일치하면 비교시작
    #boom 단어와 비교후 일치하면 스택에서 그만큼 삭제하고 스택에 추가
    if char == lastchar and ''.join(stack[-length:])==boom:
        del stack[-length:]
result=''.join(stack)
    

if(result==""):
    print("FRULA")
else:    
    print(result)
    
#https://mytodays.tistory.com/23
