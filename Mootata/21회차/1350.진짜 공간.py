n = int(input()) # 파일의 개수 n
files = list(map(int, input().split())) # 파일의 크기
cluster = int(input()) # 클러스터의 크기

result = 0
for i in files :
    if i % cluster > 0 :
        result += i // cluster + 1
    else :
        result += i // cluster

print(cluster * result)