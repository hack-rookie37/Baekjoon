n = int(input())

numbers = 1
answer = 1
while n > numbers :
    numbers += 6 * answer
    answer += 1
print(answer)