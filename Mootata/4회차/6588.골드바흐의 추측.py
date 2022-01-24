is_prime = [True for _ in range(1000001)]
    
for i in range(2, 1001):
    if is_prime[i]:
        for j in range(i * 2, 1000001, i):
            is_prime[j] = False
            
while True:
    number = int(input())
    if_find = False
    
    if number == 0:
        break
    
    for i in range(3, len(is_prime)):
        if is_prime[i] and is_prime[number - i]: # 어차피 입력 받은 값을 찾는 것이기 때문에 서로 값을 1씩 높이고 낮추면서 탐색함 (두 값의 합은 변함이 없음)
            print(number, '=', i, '+', number - i)
            is_find = True
            break
    
    if is_find == False:
        print("Goldbach's conjecture is wrong.")