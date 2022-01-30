n = int(input()) # 이동하려고 하는 채널 n
m = int(input()) # 고장난 버튼의 개수 m
answer = abs(100 - n) # +, - 버튼으로만 이동하는 경우

if m != 0:
    broken_button = list(input().split())
else:
    broken_button = []

for number in range(1000001): # 채널 0번부터 1000001까지
    for i in str(number): # 예를들어 number가 10001이라면 i는 1, 0, 0, 1
        if i in broken_button: # 해당하는 번호가 고장난 버튼이라면
            break
    else:
        answer = min(answer, len(str(number)) + abs(number - n)) # 누를 수 있는 채널까지는 누르고, 해당 채널 - 이동하려는 채널
            
print(answer)