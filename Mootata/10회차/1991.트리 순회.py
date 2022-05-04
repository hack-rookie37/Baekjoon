import sys

input = sys.stdin.readline

n = int(input()) # 노드의 개수 n
tree = {}

for i in range(n):
    root, child1, child2 = input().split()
    tree[root] = (child1, child2) # 딕셔너리 root를 키로 자식 노드들을 값으로

def preorder(node):
    if node == '.':
        return
    print(node, end='') # 현재 노드 출력(root) 
    preorder(tree[node][0]) # 왼쪽의 자식 노드부터 탐색
    preorder(tree[node][1]) # 이후 오른쪽의 자식 노드 탐색

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) # 왼쪽의 자식 노드로 계속 이동하다가 위의 if문에서 .을 만나면 return
    print(node, end='')
    inorder(tree[node][1]) # 왼쪽의 자식 노드들의 탐색이 끝났다면 오른족 시작

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')