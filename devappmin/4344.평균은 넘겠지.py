loop = int(input())

for i in range(loop):
    m = list(map(int, input().split()))
    l = [x for x in m[1:] if x >( sum(m[1:]) / m[0])]
    print("%.3f%%" % round(len(l) / m[0] * 100, 3))