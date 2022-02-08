import sys

n, m = map(int, sys.stdin.readline().split()) # 수의 개수 n, 합을 구해야 하는 횟수 m
numbers = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
value = 0

for i in range(n):
    value += numbers[i]
    prefix_sum.append(value)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i - 1]) # a ~ b까지의 합은 결국 첫번째 수부터 b번째 수 까지 더한 값에서
                                             # 첫번째 수부터 a - 1번째 까지 수를 빼준 것과 같음 따라서 미리 모든 누적 합을 구해놓고
                                             # 이것을 사용해서 구간 합을 구함