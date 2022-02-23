import sys
input = sys.stdin.readline

test_case = int(input())

def solution():
    count = int(input())
    people = sorted([tuple(map(int, input().split())) for x in range(count)])
    ans = 1
    m = people[0][1]
    for i in range(1, count):
        if m > people[i][1]:
            ans += 1
            m = people[i][1]
    print(ans)

for i in range(test_case):
    solution()