n, q = map(int, input().split()) # 악보 수 N, 질문의 개수 Q
sheet = [int(input()) for _ in range(n)]

for _ in range(q):
    t = int(input())
    for i in range(n):
        if t < sum(sheet[:i + 1]):
            print(i + 1)
            break