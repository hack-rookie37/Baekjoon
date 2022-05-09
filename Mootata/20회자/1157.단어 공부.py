word = input().strip().upper()
alph = list(set(word))
count = [0] * len(alph)
index = 0

for i in alph:
    count[index] = word.count(i)
    index += 1

if count.count(max(count)) > 1:
    print('?')
else:
    print(alph[count.index(max(count))])