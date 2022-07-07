import sys

n = int(sys.stdin.readline())
dists = [int(sys.stdin.readline()) for _ in range(n)]
total_dist = sum(dists)

left, right = 0, 0
inner_dist = dists[0]
answer = 0

while left <= right and right < n:
    outer_dist = total_dist - inner_dist
    answer = max(answer, min(outer_dist, inner_dist))

    if inner_dist < outer_dist:
        right += 1
        if right < n:
            inner_dist += dists[right]
    else:
        inner_dist -= dists[left]
        left += 1

print(answer)