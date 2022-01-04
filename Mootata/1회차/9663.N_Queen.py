def n_queen(i): # i는 현재 행을 의미
    global case
    if i == n: # 현재 행이 마지막 행인 경우, = 탐색이 모두 끝났다는 뜻
        case += 1
        return
    for j in range(n): # 각 열에 퀸을 놓는 경우의 수를 확인
        col[i] = j # i행 j열에 퀸을 놓음
        if promising(i): # i행 j열에 퀸을 놓는 경우 유망한지 확인 (겹치는 퀸이 있는지 확인)
            n_queen(i + 1) # 겹치는 퀸이 없다면 다음 행으로 이동 해서 다시 각 열에 퀸을 놓는 경우를 확인
            
def promising(i): # 퀸이 다른 퀸을 공격할 수 있는지 확인 i는 행
    for j in range(i):                                        # col[i] == col[j] -> 같은 열에 놓이는 경우 
        if col[i] == col[j] or abs(col[i] - col[j]) == i - j: # abs(col[i] - col[j]) == i - j 열의 차이의 절대값과 행의차이가 같다면
            return False                                      # 같은 대각선에 놓였다는 뜻 
    return True # 위의 조건식이 만족되지 않는다면 유망하다고 판단 True 리턴

n = int(input()) # n x n 크기의 체스판 위에 n개의 퀸
case = 0 # N개의 퀸이 서로 공격할 수 없게 놓는 경우의 수 
col=[0] * n # 깊이가 n인 트리 생성, col[i] = j 는 i행 j열에 퀸을 놓았다는 뜻(j가 0인 경우 비어있는 칸)
n_queen(0)
print(case)