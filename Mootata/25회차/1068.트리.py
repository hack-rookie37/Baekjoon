from collections import deque

n = int(input()) # 트리의 노드의 개수 N
nodes = list(map(int, input().split()))
r = int(input()) # 지울 노드의 번호
tree = [[] for i in range(n)]
root = 0

for i in range(n):
    if nodes[i] == -1:
        root = i
        continue
    tree[nodes[i]].append(i)

if r == root:
    print(0)
    exit(0)

def bfs():
    q = deque()
    q.append(root)
    answer = 0
    
    while q:
        node = q.popleft()
        
        if not tree[node] or (len(tree[node]) == 1 and tree[node][0] == r): # 자식노드가 없거나, 노드가 1개 있지만 삭제할 노드인 경우 leaf노드이므로 answer +1
            answer += 1
            continue
        
        for i in tree[node]:
            if i != r: # 삭제할 노드는 탐색 안함
                q.append(i)
    
    return answer

print(bfs())