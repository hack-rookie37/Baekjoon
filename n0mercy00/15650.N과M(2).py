from itertools import combinations
import itertools

a,b=input().split() #입력을 받아서 두개로 쪼개기
items=list(range(1,int(a)+1)) #처음 입력받은 숫자만큼 까지 

nCr=itertools.combinations(items,int(b)) #콤비네이션 aCb

#결과물 출력하는데 필요없는 기호 잘라주기
for i in list(nCr):
    print(str(i).strip("("")").replace(',',''))
    