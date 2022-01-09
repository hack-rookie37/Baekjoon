N, M = map(int, input().split())
trees = list(map(int, input().split()))


def chop(M, trees):
    h_min, h_max = 0, max(trees)
    max_H = 0

    while h_min != h_max - 1:
        length = 0
        H = (h_min + h_max) // 2
        for t in trees:
            length += t - H if t > H else 0

        if length == M:
            return H
        elif length < M:
            h_max = H
        else:
            h_min = H
            max_H = max(max_H, H)
    return max_H


print(chop(M, trees))
