from itertools import product


def sol():
    cases = []

    for ti, tj in teachers:
        for si, sj in students:
            temp = []
            changed = False

            if ti == si:
                temp = [(ti, k) for k in range(min(sj, tj) + 1, max(sj, tj))]
                changed = True

            if tj == sj:
                temp = [(k, tj) for k in range(min(si, ti) + 1, max(si, ti))]
                changed = True

            if changed:
                if len(temp) == 0:
                    return "NO"
                cases.append(list(temp))

    for answer in product(*cases):
        if len(set(answer)) <= 3:
            return "YES"

    return "NO"


N = int(input())
corr = [list(input().split()) for _ in range(N)]
teachers, students = [], []

for i in range(N):
    for j in range(N):
        if corr[i][j] == "T":
            teachers.append((i, j))
        elif corr[i][j] == "S":
            students.append((i, j))

print(sol())
