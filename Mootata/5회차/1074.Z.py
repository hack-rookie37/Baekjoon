n, r, c = map(int, input().split())
answer = 0

while n != 0:
    
	n -= 1

	if r < 2 ** n and c < 2 ** n: # 1사분면
		answer += ( 2 ** n ) * ( 2 ** n ) * 0

	elif r < 2 ** n and c >= 2 ** n: # 2사분면
		answer += ( 2 ** n ) * ( 2 ** n ) * 1
		c -= ( 2 ** n )
    
	elif r >= 2 ** n and c < 2 ** n: # 3사분면
		answer += ( 2 ** n ) * ( 2 ** n ) * 2
		r -= ( 2 ** n )

	else: # 4사분면
		answer += ( 2 ** n ) * ( 2 ** n ) * 3
		r -= ( 2 ** n )
		c -= ( 2 ** n )
    
print(answer)

# 배열을 계속 4등분 해서 찾고있는 좌표가 어느 사분면에 해당하는지 찾음