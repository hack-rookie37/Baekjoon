import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split()) # 사람의 수 n, 파티의 수 m
party_members = [[] for _ in range(n + 1)] # 파티에 참가하는 사람들 중에 이야기가 퍼질 수 있는 경로
partys = [[] for _ in range(m)] # 파티의 목록 (각 파티에 누가 참석했는지)
visited = [False for _ in range(n + 1)]
know_story = [] # 진실을 알고 있는 사람들
answer = set() # set으로 만들어서 중복 제거 진실을 알고 있던 사람 + 알게된 사람
q = deque()

for j in list(map(int, input().split()))[1:]:
    know_story.append(j)
    answer.add(j)

for i in range(m): # 파티에 함께 참석한 사람들
    people = list(map(int, input().split()))
    partys[i] = (people[1:])
    for j in range(1, people[0]):
        party_members[people[j]].append(people[j + 1]) # 예를들어 1과 2가 파티에 참석했다면.
        party_members[people[j + 1]].append(people[j]) # people[1]에는 2를 넣고, people[2]에는 1을 넣음

def bfs():
    while q:
        v = q.popleft()
        for i in party_members[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                answer.add(i) # 진실을 아는 사람과 함께 참석한 사람은 진실을 알게되므로 answer에 추가

for i in know_story: # 진실을 아는 사람들부터 탐색
    q.append(i) # 미리 큐에 담아줌

bfs()

for i in partys:
    for j in i:
        if j in answer:
            m -= 1 # 진실을 아는 사람이 포함된 파티는 파티 수 m에서 빼줌
            break

print(m)