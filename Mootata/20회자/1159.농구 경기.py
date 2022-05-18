from collections import defaultdict

n = int(input())
players = [list(input().strip()) for _ in range(n)]
dict = defaultdict(int)
answer = ''


for i in range(n):
    dict[players[i][0]] += 1

for i in dict:
    if dict[i] >= 5:
        answer += i

if answer == '':
    print('PREDAJA')
else:
    print(*sorted(answer), sep='')