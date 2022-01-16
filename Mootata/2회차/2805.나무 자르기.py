n, m = map(int, input().split()) # n 나무의 수, m 필요한 나무의 길이
height = list(map(int, input().split())) # 각 나무의 높이
start, end = 0, max(height) # 벌목기의 첫 높이는 가장 긴 나무의 절반 높이
height.sort() # 나무 높이순으로 정렬

while start <= end:
    mid = (start + end) // 2
    length = 0 #벌목된 나무의 길이
    
    for i in height:
        if i > mid: # 나무의 높이가 mid보다 크면 잘라냄
            length += i - mid # 잘라낸 나무의 길이 더함
            
    if length >= m: # 필요한 길이보다 길거나 같으면 더 높게 설치
        start = mid + 1
    else: # 짧다면 더 낮게 설치
        end = mid - 1
        
print(end)