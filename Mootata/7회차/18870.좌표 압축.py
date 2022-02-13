import sys

input = sys.stdin.readline

n = int(input()) # 좌표의 개수 n
locations = list(map(int, input().split()))
sorted_set = list(sorted(set(locations))) # sorted_set은 중복을 제거하고 정렬시킨 리스트
dic = {sorted_set[i]: i for i in range(len(sorted_set))} #  정렬된 순서대로 리스트의 값을 키로하고 인덱스(몇번째로 큰 값인지)를 값으로 해서 딕셔너리에 넣어줌 

for i in locations: # 좌표를 하나씩 꺼내서 딕셔너리에서 검색하면, 값으로 해당 값이 몇번째로 큰 값인지 출력함
    print(dic[i], end = ' ')