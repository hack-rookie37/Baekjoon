import sys

sys.setrecursionlimit(10 ** 6) # 재귀 깊이 늘려줌
input = sys.stdin.readline

nodes = []

while True:
    try:
        nodes.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    root = nodes[start]
    index = start + 1
    
    while index <= end: # 루트보다 커지는 값 찾기
        if nodes[index] > root:
            break
        index += 1
        
    postorder(start + 1, index - 1) # 왼쪽
    postorder(index, end) # 오른쪽
    
    print(root) # 후위 순회라 마지막에 출력

postorder(0, len(nodes) - 1)

# 전위 50 - 30 - 24 - 5 - 28 - 45 - 98 - 52 - 60
# 후위 5 - 28 - 24 - 45 - 30 - 60 - 52 - 98 - 50

# 전위 순회의 특성상, 맨 처음 값은 root이고 root보다 큰 값중 맨처음 나오는 98을 포함한, 오른쪽
# 값들은 모두 오른쪽 서브트리임.