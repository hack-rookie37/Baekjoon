from itertools import permutations

def split_expr(expression):
    expr = []
    num = ''
    operators = set()
    for e in expression:
        if not e.isdecimal():
            expr.append(num)
            expr.append(e)
            operators.add(e)
            num = ''
        else:
            num += e
    expr.append(num)
    return expr, operators

def solution(expression):
    expr, operators = split_expr(expression)
    conditions = list(permutations(operators, len(operators)))
    answer = []
    
    for case in conditions:
        temp = list(expr)
        for op in case:
            i = 0
            while i < len(temp) - 1:
                if temp[i] == op:
                    cal = str(eval(temp[i-1] + temp[i] + temp[i+1]))
                    temp = temp[:i-1] + [cal] + temp[i+2:]
                else:
                    i += 1

        answer.append(abs(int(*temp)))

    return max(answer)