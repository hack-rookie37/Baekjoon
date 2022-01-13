pay = int(input())
change = 1000 - pay
count = 0
unit = [500, 100, 50, 10, 5, 1]

for coin in unit:
    count += change // coin
    change %= coin

print(count)