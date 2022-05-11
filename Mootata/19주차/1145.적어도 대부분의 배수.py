numbers = list(map(int, input().split()))
check = min(numbers)

while True:
    count = 0
    
    for i in numbers:
        if check % i == 0:
            count += 1
            
    if count >= 3:
        print(check)
        break
    
    check += 1