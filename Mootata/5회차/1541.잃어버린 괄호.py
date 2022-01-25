formula = input().split('-')
minus = []
answer = 0

plus = map(int, formula[0].split('+')) #-를 기준으로 리스트에 담았기 떄문에 리스트의 첫번째 값은 더해줌
answer += sum(plus)

for i in range(1, len(formula)):
    minus = (map(int, formula[i].split('+'))) # 마찬가지로 두번째 값 부터는 더해서 뺴줌
    answer -= sum(minus)
    
print(answer)