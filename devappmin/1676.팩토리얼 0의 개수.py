import math
l = list(str(math.factorial(int(input())))[::-1])
ll = []
for c in l:
    if c == '0':
        ll.append(c)
    else:
        break
print(len(ll))