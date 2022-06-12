N, L = map(int, input().split())
leak = sorted(map(int, input().split()))
start = leak[0]
tape = 1

for i in range(1, N):
    if leak[i] - start + 1 <= L:
        continue
    else:
        tape += 1
        start = leak[i]

print(tape)
