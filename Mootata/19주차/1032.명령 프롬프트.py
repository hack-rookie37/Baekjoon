n = int(input()) # 파일 이름의 개수 N
name = list(input())

for i in range(n - 1):
    searching = list(input())
    for j in range(len(name)):
        if name[j] != searching[j]:
            name[j] = '?'
print(''.join(name))