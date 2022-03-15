import sys
cases = int(sys.stdin.readline().rstrip("\n"))
for _ in range(cases):
    days = int(sys.stdin.readline().rstrip("\n"))
    price = list(map(int, sys.stdin.readline().rstrip("\n").split()))
    surplus=0
    lastPrice=0
    for i in range(len(price)-1,-1,-1):
        #가격이 떨어졌다면 ->전날의 가격이 더 높다면
        if(price[i] > lastPrice):
            #흑자 놋땃쥐
            lastPrice = price[i]
        else:
            #아니면 차익만큼 파라~
            surplus+=lastPrice-price[i]
    print(surplus)