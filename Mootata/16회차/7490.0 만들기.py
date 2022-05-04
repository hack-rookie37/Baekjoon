import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    answer = [numbers[0]]
    answers = []
    q.append((1, answer))
    
    while q:
        count, answer = q.popleft()
        answer1 = answer[:] # answer 하나로 pop하면서 쓰려고 했는데 큐에 들어간 answer에서도 
        answer2 = answer[:] # 값이 빠져버려서 그냥 answer 3개 만듬
        answer3 = answer[:]
        if count < n:
            answer1.append('+' + numbers[count])
            q.append((count + 1, answer1)) # +
            answer2.append('-' + numbers[count])
            q.append((count + 1, answer2)) # -
            answer3.append(' ' + numbers[count])
            q.append((count + 1, answer3)) # ' '
        
        else: # 수식이 완성되면 
            formula = []
            num = 0
            index = 0
            for i in range(n):
                if ' ' in answer[i]: # 공백이 들어있으면 
                    index += 1 # pop을 사용하기 때문에 인덱스 에러 방지하기 위해 만듬
                    if int(formula[i - index]) >= 0: # 합쳐야 하는 앞의 숫자가 양수일 때
                        formula.append((formula[i - index] * 10) + int(answer[i]))
                        formula.pop(i - index) # 앞의 숫자와 합친 것이기 때문에 해당 숫자는 삭제
                    else: # 음수일 때
                        formula.append((formula[i - index] * 10) - int(answer[i]))
                        formula.pop(i - index)
                else: # +, - 일때는 그냥 append
                    formula.append(int(answer[i]))
            
            for j in formula: # 만들어진 수식 계산
                num += j
            if num == 0: # 바로 출력하려고 했는데 문제에서 ASCII 순서에 따라 출력하라고 해서
                answers.append(''.join(answer))
    return sorted(answers) # 모아서 정렬 후 return

for t in range(int(input())):
    n = int(input()) # 1부터 n까지의 자연수
    numbers = sorted(list(str(i) for i in range(1, n + 1)))
    
    for i in bfs():
        print(*i, sep='')
    print()