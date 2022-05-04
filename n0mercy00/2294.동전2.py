from sys import stdin
n, k = map(int, stdin.readline().split())
coins=[]
dp=[10001]*(k+1) #얘 뜻머임 얘 왜 없으면 안되지
dp[0]=0

for i in range(n):
    coins.append(int(input()))
    
for nowCoin in coins:
    for i in range(nowCoin,k+1):
        dp[i]=min(dp[i],dp[i-nowCoin]+1)

if dp[k] == 10001:
       print(-1)
else:
   print(dp[k])

#점화식이 dp[i]=min(dp[i-Coin])+1 임 
#뭔소리냐하면 ex) 6원 = 5원+ 1원 ->dp[6]=min(dp[6-5])+1