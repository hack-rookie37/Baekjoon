import math

n = int(input())
count = 0

number = list(str(math.factorial(n)))

for i in number[::-1]:
    if i == '0':
        count += 1
    else:
        break
    
print(count)