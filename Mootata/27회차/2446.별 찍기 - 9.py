n = int(input())

for i in range(n):
    print(" " * i, "*" * (2 * (n - i) - 1), sep="")
for i in range(n-2, -1, -1):
    print(" " * i, "*" * (2 * (n - i) - 1), sep="")