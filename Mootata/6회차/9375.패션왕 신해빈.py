t = int(input()) # 테스트 케이스 수 t

for i in range(t):
    n = int(input())
    costume = {}
    
    for j in range(n):
        clothes = list(input().split())
        if clothes[1] in costume: # cosutme 딕셔너리에 입력받은 옷의 종류가 존재한다면 
            costume[clothes[1]].append(clothes[0]) # 거기에 옷을 추가해주고
        else:
            costume[clothes[1]] = [clothes[0]] # 없다면 새로 만듬
            
    count = 1
    
    for k in costume:
        count *= (len(costume[k]) + 1) # 옷의 종류수에 +1 한 값을 모두 곱해주고
    print(count - 1)                   # 아무것도 입지 않는 경우를 뻬줌
    print(costume)