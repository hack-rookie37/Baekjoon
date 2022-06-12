from collections import deque, defaultdict

n, k = map(int, input().split()) # 수빈이의 위치 N, 동생의 위치 K
answer = defaultdict(int)

def bfs():
    q = deque()
    q.append((n, 0))
    visited = [False for _ in range(100001)]
    
    while q:
        current_n, count = q.popleft()
        visited[current_n] = True
        
        if current_n == k:
            if len(answer) <= 1:
                answer[count] += 1
            else:
                return list(answer.keys())
        
        else:
            if current_n + 1 <= 100000 and not visited[current_n + 1]:
                q.append((current_n + 1, count + 1))
                
            if current_n - 1 >= 0 and not visited[current_n - 1] :
                q.append((current_n - 1, count + 1))
                
            if current_n * 2 <= 100000 and not visited[current_n * 2]:
                q.append((current_n * 2, count + 1))
                
    return list(answer.keys())

l = bfs()
print(l[0], answer[l[0]], sep = '\n')

# 목표 위치에 도달하는 시간을 키값, 방법의 수를 밸류로 같는 딕셔너리를 만듬
# 가장 작은 키값과 밸류가 답