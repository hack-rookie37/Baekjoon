# while True:
#     weight = input("3~5000 사이의 정수를 입력하세요 : ") # weight = N
#     if weight.isdigit():
#         weight = int(weight)
#         if weight < 3 or weight > 5000:
#             print("3보다 작거나 5000보다 큰 값이 입력되었습니다.")
#         else:
#             _5_remainder = weight % 5 # 5로 나눈 나머지
#             _3_remainder = weight % 3 # 3으로 나눈 나머지
#             break
#     else:
#         print("문자열이나 음수가 아닌 정수를 입력해주세요.")

# 백준 채점 용

weight = int(input())
_5_remainder = weight % 5 
_3_remainder = weight % 3
if _5_remainder == 0: # 5로 나누어 떨어질 떄
    answer = weight / 5
    print(int(answer))
elif _5_remainder != 0: # 5로 나누어 떨어지지 않을 때
    weight_value = weight
    answer = 1
    while (weight_value % 5) % 3 != 0: # 5와 3으로 나누어 떨어지는 경우가 있는지
        weight_value = weight_value - 3
        answer = answer + 1
        if weight_value < 5:
            break
    if weight_value >= 5:
        answer = (weight_value / 5) + answer
        print(int(answer))
    elif _3_remainder == 0: # 3으로 나눈 값이 답인 경우는 가장 비효율 적인 경우기 때문에 마지막에 실행
        answer = weight / 3
        print(int(answer))
    else:
        print(-1)