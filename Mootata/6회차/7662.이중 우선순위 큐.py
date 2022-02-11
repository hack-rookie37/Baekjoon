from heapq import heappush, heappop

for t in range(int(input())):
    k = int(input()) # 연산의 개수 k
    minq = [] # 최소
    maxq = [] # 최대
    visited = [False] * 1000001
    
    for i in range(k):
        calculate, value = input().split() # 연산의 종류 calculate, 값 value
        if calculate == 'I':
            heappush(minq, (int(value), i))
            heappush(maxq, (-1 * int(value), i))
            visited[i] = True
        else:
            if value == '-1' and minq:
                while minq and not visited[minq[0][1]]:
                    heappop(minq)
                if minq:
                    visited[minq[0][1]] = False
                    heappop(minq)
            elif value == '1' and maxq:
                while maxq and not visited[maxq[0][1]]:
                    heappop(maxq)
                if maxq:
                    visited[maxq[0][1]] = False
                    heappop(maxq)
    while minq and not visited[minq[0][1]]:
        heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heappop(maxq)
    
    if minq and maxq:
        print(-1 * maxq[0][0], minq[0][0])
    else:
        print('EMPTY')        
                

# 최소힙, 최대힙 두개를 만들고, 최댓값을 삭제할떄는 최대힙에서, 최솟값을 삭제할때는 최소합에서 삭제한다
# 마지막에 최대, 최솟값을 출력할때도 최솟값은 최소힙에서, 최댓값은 최대힙에서 출력한다.

# 동기화를 안해줘서 틀렸었음