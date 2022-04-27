import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input()) # 단어의 개수 N
words = [list(input().strip()) for _ in range(n)]
dic = defaultdict(int)
answer = 0
num = 9

for word in words:
    index = 0
    for i in range(len(word) - 1, -1, -1):
        dic[word[index]] += 10 ** i
        index += 1

for i in sorted(dic.values(), reverse = True):
    answer += i * num
    num -= 1

print(answer)