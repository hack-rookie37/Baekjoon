import sys

n = int(sys.stdin.readline())
nums = sorted(list(sys.stdin.readline().split()), key=lambda a: a * 10, reverse=True)
print(str(int(''.join(nums))))

# 프로그래머스 정렬 - 가장 큰 수 (level2)와 동일한 문제