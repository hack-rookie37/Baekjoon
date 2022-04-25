import sys

input = sys.stdin.readline

n, p = map(int, input().split()) # 멜로디에 포함된 음의 수 N, 한 줄에 있는 프렛의 수 P
melody = [tuple(map(int, input().split())) for _ in range(n)]
stacks = [[] for _ in range(500001)]
count = 0

for string, flat in melody:
    if not stacks[string]:
        stacks[string].append(flat)
        count += 1
    elif stacks[string][-1] == flat:
        continue
    elif stacks[string][-1] < flat:
        stacks[string].append(flat)
        count += 1
        
    elif stacks[string][-1] > flat:
        while stacks[string] and stacks[string][-1] > flat:
            stacks[string].pop()
            count += 1
        if stacks[string]:
            if stacks[string][-1] != flat:
                stacks[string].append(flat)
                count += 1
        else:
            stacks[string].append(flat)
            count += 1

print(count)