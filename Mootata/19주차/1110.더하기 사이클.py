n = int(input())
num = n
count = 0

while True:
    digit_10 = (num // 10)
    digit_1 = num % 10
    
    count += 1
    num = (digit_1 * 10) + ((digit_10 + digit_1) % 10)
    
    if n == num:
        print(count)
        break