s = int(input()) # 자연수 S
num = 0
answer = 0

while True:
    answer += 1
    num += answer
    if num > s:
        answer -= 1
        break

print(answer)