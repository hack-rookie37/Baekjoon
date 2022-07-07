n, m, b = map(int, input().split()) # N x M 크기의 집터, B개의 블록
land = [list(map(int, input().split())) for _ in range(n)]
h = 0
answer = float('inf')


for i in range(257): # 높이 0 ~ 256까지
    plus, minus = 0, 0
    
    for j in range(n):
        for k in range(m):
            if land[j][k] < i: # 블록의 높이가 현재 높이보다 낮다면
                minus += i - land[j][k] # 높이 i에 맞추기 위해 필요한 블록의 개수
            else:
                plus += land[j][k] - i # 높이 i에 맞추기 위해 빼야하는 블록의 개수
    inv = b + plus # 인벤토리에 들어있는 블록의 수
    
    if inv < minus: # 빼야하는 블록보다 인벤토리의 블록이 적다면 땅고르기 실패
        continue
    time = 2 * plus + minus # 땅고르기가 가능하다면 걸리는 시간 체크
    
    if time <= answer:
        answer = time
        h = i # 높이 0부터 확인하기 때문에 항상 더 높은 층의 땅고르기 결과가 저장됨

print(answer, h)