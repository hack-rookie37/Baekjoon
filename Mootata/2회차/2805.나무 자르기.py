n, m = map(int, input().split()) # n 나무의 수, m 필요한 나무의 길이
height = list(map(int, input().split())) # 각 나무의 높이
start, end = 1, max(height) # 최소 높이 1 start, 집 앞 나무들 중 가장 높은 나무의 높이 end
height.sort() # 나무 높이순으로 정렬

while start <= end:
    mid = (start + end) // 2
    length = 0 #벌목된 나무의 길이
    
    for i in height:
        if i > mid: # 나무의 높이가 mid보다 크면 잘라냄
            length += i - mid # 잘라낸 나무의 길이 더함
            
    if length >= m: # 위의 연산을 통해 잘라낸 나무길이의 총합이 필요한 길이보다 크거나 같으면 오른쪽에서 찾음
        start = mid + 1
    else: # 작다면 왼쪽에서 찾음
        end = mid - 1
        
print(end)