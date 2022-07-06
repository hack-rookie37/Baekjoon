h, w = map(int, input().split())
blocks = list(map(int, input().split()))
highest = blocks.index(max(blocks))
lh, rh = blocks[0], blocks[-1]
answer = 0

for block in blocks[:highest + 1]:
    lh = max(lh, block)
    
    answer += lh - block

for block in list(reversed(blocks))[:highest]:
    rh = max(rh, block)
    
    answer += rh - block

print(answer)