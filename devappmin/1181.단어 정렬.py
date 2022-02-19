import sys

n = int(sys.stdin.readline())
words = [] 

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append((len(word), word))

words = sorted(set(words))

print(*[word for _, word in words], sep="\n")
