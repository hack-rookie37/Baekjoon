P, K = map(int, input().split())
a = Truefor i in range(2,K):    if P % i == 0:        print('BAD', i)        a = False        breakif a:    print('GOOD')
