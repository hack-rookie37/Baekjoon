from collections import defaultdict, deque

N = int(input())
tree = defaultdict(list)

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

parents = [True] * 2 + [False] * (N - 1)

queue = deque([1])
while queue:
    node = queue.popleft()
    for child in tree[node]:
        if not parents[child]:
            parents[child] = node
            queue.append(child)

print(*parents[2:], sep="\n")
