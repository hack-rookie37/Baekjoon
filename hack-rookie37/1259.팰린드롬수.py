import sys

answer = []

while True:
    tc = sys.stdin.readline().strip()
    if tc == "0":
        break
    end = len(tc)
    k = end // 2
    for i in range(k):
        if tc[i] != tc[end - i - 1]:
            break
    else:
        answer.append("yes")
        continue
    answer.append("no")

print(*answer, sep="\n")
