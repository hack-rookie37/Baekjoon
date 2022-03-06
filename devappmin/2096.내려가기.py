import sys

n = int(sys.stdin.readline())

dp_max = [(0, 0, 0), (0, 0, 0)]
dp_min = [(0, 0, 0), (0, 0, 0)]

idx = 0

for idx in range(n):
    a, b, c = map(int, sys.stdin.readline().split())

    dp_max[idx % 2]

    if idx % 2 == 0:
        dp_max[0] = ((max(dp_max[1][0] + a, dp_max[1][1] + a),
                      max(dp_max[1][0] + b, dp_max[1]
                          [1] + b, dp_max[1][2] + b),
                      max(dp_max[1][1] + c, dp_max[1][2] + c)))
        dp_min[0] = ((min(dp_min[1][0] + a, dp_min[1][1] + a),
                      min(dp_min[1][0] + b, dp_min[1]
                          [1] + b, dp_min[1][2] + b),
                      min(dp_min[1][1] + c, dp_min[1][2] + c)))
    else:
        dp_max[1] = ((max(dp_max[0][0] + a, dp_max[0][1] + a),
                     max(dp_max[0][0] + b, dp_max[0][1] + b, dp_max[0][2] + b),
                     max(dp_max[0][1] + c, dp_max[0][2] + c)))
        dp_min[1] = ((min(dp_min[0][0] + a, dp_min[0][1] + a),
                      min(dp_min[0][0] + b, dp_min[0]
                          [1] + b, dp_min[0][2] + b),
                      min(dp_min[0][1] + c, dp_min[0][2] + c)))

print(max(dp_max[idx % 2]), min(dp_min[idx % 2]))
