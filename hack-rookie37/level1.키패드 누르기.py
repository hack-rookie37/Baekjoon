def solution(numbers, hand):
    answer = ""

    lfinger = [3, 0]
    rfinger = [3, 2]

    for num in numbers:
        cood = [(num - 1) // 3, (num - 1) % 3]

        if num in (1, 4, 7):
            answer += "L"
            lfinger = cood
        elif num in (3, 6, 9):
            answer += "R"
            rfinger = cood
        else:
            if num == 0:
                cood = [3, 1]

            left = abs(cood[0] - lfinger[0]) + abs(cood[1] - lfinger[1])
            right = abs(cood[0] - rfinger[0]) + abs(cood[1] - rfinger[1])

            if left < right:
                lfinger = cood
                answer += "L"
            elif left > right:
                rfinger = cood
                answer += "R"
            else:
                if hand == "left":
                    lfinger = cood
                    answer += "L"
                else:
                    rfinger = cood
                    answer += "R"

    return answer
