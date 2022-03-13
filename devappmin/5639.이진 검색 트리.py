import sys
sys.setrecursionlimit(10 ** 6)

nodes = []

while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break


def post_order(left_node, right_node):
    if left_node > right_node:
        return

    mid_node = right_node + 1

    for idx in range(left_node + 1, right_node + 1):
        if nodes[left_node] < nodes[idx]:
            mid_node = idx
            break

    post_order(left_node + 1, mid_node - 1)
    post_order(mid_node, right_node)
    print(nodes[left_node])


post_order(0, len(nodes) - 1)


# 아래는 불합격한 코드
# import sys

# nodes = {}

# while True:
#     try:
#         node = int(sys.stdin.readline())
#         if not nodes:
#             root = node
#             nodes[root] = ['.', '.']
#             continue

#         current_pos = root

#         while True:
#             if current_pos > node:
#                 if nodes[current_pos][0] == '.':
#                     nodes[current_pos][0] = node
#                     nodes[node] = ['.', '.']
#                     break
#                 else:
#                     current_pos = nodes[current_pos][0]
#             else:
#                 if nodes[current_pos][1] == '.':
#                     nodes[current_pos][1] = node
#                     nodes[node] = ['.', '.']
#                     break
#                 else:
#                     current_pos = nodes[current_pos][1]
#     except:
#         break


# def post_order(node):
#     if nodes[node][0] != '.':
#         post_order(nodes[node][0])

#     if nodes[node][1] != '.':
#         post_order(nodes[node][1])

#     print(node)


# post_order(root)

# # 50 30 24 5 28 45 98 52 60
