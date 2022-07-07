n = int(input())
points = []

for _ in range(n):
    points.append(int(input()))

s = sum(points)

left, right = 0, 0
answer = 0
current = points[0]

while left <= right and right < n:
    m = min(current, s - current) # 시계 방향, 반시계 방향의 거리 중 더 작은 것
    answer = max(answer, m)
    
    if current == m: # 시계 방향으로의 타워간의 거리가 더 짧다면, right를 한칸 이동
        right += 1
        if right < n:
            current += points[right]
    else: # 반시계 방향으로의 타워간의 거리가 더 짧아졌다면, left를 한칸 이동
        current -= points[left]
        left += 1

print(answer)