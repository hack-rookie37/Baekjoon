import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[in_order[i]] = i

def pre_order(in_s, in_e, post_s, post_e):
    if (in_s > in_e) or (post_s > post_e):
        return
    
    parent = post_order[post_e]
    print(parent, end=" ")
    
    left = pos[parent] - in_s
    right = in_e - pos[parent]
    
    pre_order(in_s, in_s + left - 1, post_s, post_s + left - 1)
    pre_order(in_e - right + 1, in_e, post_e - right, post_e - 1)

pre_order(0, n - 1, 0, n - 1)