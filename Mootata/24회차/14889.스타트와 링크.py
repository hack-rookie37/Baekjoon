from itertools import combinations

n = int(input())
player = list(range(n))
team = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

for s in combinations(player, n // 2): # 팀이 만들어지는 경우의 수
    l = list(set(player) - set(s)) # 그렇게 만들어진 팀원을 제외한 나머지로 구성된 팀
    start, link = 0, 0
    for i, j in combinations(s, 2): # 각각의 팀원끼리의 시너지 점수의 모든 합
        start += team[i][j]
        start += team[j][i]
    for i, j in combinations(l, 2):
        link += team[i][j]
        link += team[j][i]
    answer = min(answer, abs(start - link))

print(answer)