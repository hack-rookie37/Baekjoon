h, w = map(int, input().split())
blocks = list(map(int, input().split()))
highest = blocks.index(max(blocks)) # 가장 높은 블록
lh, rh = blocks[0], blocks[-1]
answer = 0

for block in blocks[:highest + 1]: # 가장 높은 블록 기준 왼쪽
    lh = max(lh, block) # 왼쪽에서 가장 높은 블록
    
    answer += lh - block

for block in list(reversed(blocks))[:len(blocks) - highest]: # 가장 높은 블록 기준 오른쪽
    rh = max(rh, block) # 오른쪽에서 가장 높은 블록
    
    answer += rh - block

print(answer)

# 가장 높은 블록을 기준으로 왼쪽, 오른쪽을 나눠서 고이는 빗물의 총량을 구함.
# 왼쪽끝의 블록을 lh에 담고, 해당 블록보다 낮으면 낮은 만큼의 빗물을 answer에 더해줌
# 진행도중 lh보다 높은 블록이 나타나면 해당 높이로 lh 초기화, highest까지 반복해서 진행.
# 오른쪽도 마찬가지로 오른쪽 끝에서부터 highest까지 진행