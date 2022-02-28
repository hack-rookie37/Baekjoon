import sys
from collections import defaultdict

n = int(sys.stdin.readline())
tree = defaultdict(list)

for _ in range(n):
    c_node, l_node, r_node = sys.stdin.readline().rstrip().split()
    tree[c_node].extend([l_node, r_node])

visited = defaultdict(bool)

def dfs(c_node, solve_type):
    visited[c_node] = True
    
    if solve_type == 0:
        print(c_node, end="")

    if not visited[tree[c_node][0]] and tree[c_node][0] != '.':
        dfs(tree[c_node][0], solve_type)
    
    if solve_type == 1:
        print(c_node, end="")
    
    if not visited[tree[c_node][1]] and tree[c_node][1] != '.':
        dfs(tree[c_node][1], solve_type)

    if solve_type == 2:
        print(c_node, end="")
    
    visited[c_node] = False

dfs('A', 0)
print()
dfs('A', 1)
print()
dfs('A', 2)


# def preorder_dfs(c_node):
#     visited[c_node] = True
#     print(c_node, end="")

#     if not visited[tree[c_node][0]] and tree[c_node][0] != '.':
#         preorder_dfs(tree[c_node][0])
    
#     if not visited[tree[c_node][1]] and tree[c_node][1] != '.':
#         preorder_dfs(tree[c_node][1])

#     visited[c_node] = False

# def preorder_traversal():
#     preorder_dfs('A')
#     print()

# def postorder_dfs(c_node):
#     visited[c_node] = True

#     if not visited[tree[c_node][0]] and tree[c_node][0] != '.':
#         postorder_dfs(tree[c_node][0])
    
#     if not visited[tree[c_node][1]] and tree[c_node][1] != '.':
#         postorder_dfs(tree[c_node][1])

#     print(c_node, end="")
#     visited[c_node] = False

# def postorder_traversal():
#     postorder_dfs('A')
#     print()

# def inorder_dfs(c_node):
#     visited[c_node] = True

#     if not visited[tree[c_node][0]] and tree[c_node][0] != '.':
#         inorder_dfs(tree[c_node][0])
    
#     print(c_node, end="")

#     if not visited[tree[c_node][1]] and tree[c_node][1] != '.':
#         inorder_dfs(tree[c_node][1])

#     visited[c_node] = False

# def inorder_traversal():
#     inorder_dfs('A')
#     print()


# preorder_traversal()
# inorder_traversal()
# postorder_traversal()