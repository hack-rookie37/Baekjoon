from sys import stdin

input = stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
belt = belt + belt[: k - 1]

start, end = 0, k
answer = 0
kind = dict()

for i in range(end):
    kind[belt[i]] = kind.get(belt[i], 0) + 1

while end < N + k - 1:
    kind[c] = 1
    LEN = len(kind.keys())
    if answer < LEN:
        answer = LEN
    if answer > k:
        break
    kind[belt[start]] = kind.get(belt[start]) - 1
    if kind[belt[start]] == 0:
        del kind[belt[start]]
    start += 1
    kind[belt[end]] = kind.get(belt[end], 0) + 1
    end += 1

print(answer)
