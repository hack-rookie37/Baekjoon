import sys

N = int(sys.stdin.readline().rstrip()) # 자연수 N 
A = list(map(int, input().split())) # 정수 A[]
M = int(sys.stdin.readline().rstrip()) # 자연수 M
B = list(map(int, input().split())) # 정수 B[]

A = A[0:N]
B = B[0:M]

A.sort() # A값 정렬

for x in B: # B의 값을 하나씩 A의 값과 비교
    start = 0
    end = len(A) - 1
    is_find = False
    
    while is_find == False: # 같은 값을 찾으면 중지
        mid = (start + end) // 2 # index 중간값
        if x == A[mid]:
            print(1)
            is_find = True
        elif x > A[mid]: # A는 정렬되어있기 때문에 x값이 A[mid]보다 크다면 오른쪽에서 찾아야 하기 떄문에
            start = mid + 1 # start 값을 변경
        elif x < A[mid]: # 마찬가지로 x값이 A[mid]보다 작다면 왼쪽에서 찾아야하므로 end값을 변경
            end = mid - 1
            
        if start > end: # 모두 탐색했다면 break
            break
        
    if is_find == False:
        print(0)
        