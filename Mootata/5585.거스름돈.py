pay = int(input(""))
change = 1000 - pay
count = 0

if change >= 500:
    count += 1
    change -= 500

if change >= 100:
    count += change // 100
    change -= (change // 100) * 100
    
if change >= 50:
    count += change // 50
    change -= (change // 50) * 50
    
if change >= 10:
    count += change // 10
    change -= (change // 10) * 10
    
if change >= 5:
    count += change // 5
    change -= (change // 5) * 5
    
if change >= 1:
    count += change

print(count)