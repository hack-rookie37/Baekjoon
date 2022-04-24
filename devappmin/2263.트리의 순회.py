import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    parents = postorder[post_end]
    print(parents, end=" ")

    left = pos[parents] - in_start
    right = in_end - pos[parents]

    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)

preorder(0, n - 1, 0, n - 1)