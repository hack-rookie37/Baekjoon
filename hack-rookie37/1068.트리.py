import sys
from collections import defaultdict

input = sys.stdin.readline


def dfs(tree, erase):
    tree[p[erase]].remove(erase)
    stack = [erase]

    while stack:
        node = stack.pop()

        if tree.get(node):
            stack += tree[node]
            del tree[node]

    p_nodes = -1
    for node in tree:
        if len(tree[node]) > 0:
            p_nodes += 1

    return sum(map(len, tree.values())) - p_nodes


def sol(erase):
    if erase == p.index(-1):
        print(0)
        return

    tree = defaultdict(list)

    for node, p_node in enumerate(p):
        tree[p_node].append(node)

    print(dfs(tree, erase))


N = int(input())
p = list(map(int, input().split()))
erase = int(input())

sol(erase)
