while True:
    n = list(map(int, list(input()))) # 호수판에 들어갈 숫자 N
    if len(n) == 1 and n[0] == 0:
        break
    answer = 1 + len(n)
    for i in n:
        if i == 1:
            answer += 2
        elif i == 0:
            answer += 4
        else:
            answer += 3
    print(answer)