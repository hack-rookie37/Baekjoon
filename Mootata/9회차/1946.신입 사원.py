import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input()) # 지원자의 숫자 n
    scores = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 1
    
    scores.sort()
    interview_scores = scores[0][1] # 현재 선발된 인원들 중 가장 높은 면접 등수
    
    for i in range(1, n):
        if interview_scores > scores[i][1]: # 선발된 인원보다 면접 등수가 높다면
            answer += 1
            interview_scores = scores[i][1]
        if interview_scores == 1:
            break

    print(answer)

# 서류 1등 면접 6등
# 서류 2등 면접 3등 
# 서류 3등 면접 2등
# 서류 4등 면접 4등
# 이 경우 1, 2, 3은 선발되지만, 4는 서류는 4등으로 1, 2, 3보다 낮고,
# 면접 등수는 1번 6등보다 높지만 2번, 3번보다 낮기 때문에 서류도, 면접도 다른 지원자보다
# 낮기 때문에 선발되지 않음