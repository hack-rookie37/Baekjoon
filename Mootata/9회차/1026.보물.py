n = int(input()) # 정수 배열 A, B의 길이 n

a = list(map(int, input().split()))
b = list(map(int, input().split()))
index_of_b = [] # 내림차순으로 정렬된 b의 인덱스 값을 넣을 리스트

def sol1():
    answer = 0

    b2 = sorted(b, reverse = True)
    a.sort()

    for i in range(n):
        answer += a[i] * b2[i]
    return answer

def sol2():
    answer = 0
    a2 = sorted(a)
    
    for i in sorted(b, reverse=True):
        index_of_b.append(b.index(i))
        
    for i in range(n):
        a[index_of_b[i]]= a2[i]
        
    for i in range(n):
        answer += (a[i] * b[i])
    
    return answer

def sol3():
    answer = 0
    for i in range(n):
        answer += (a.pop(a.index(min(a))) * b.pop(b.index(max(b))))
    return answer

print(sol3())

# sol1
# 처음에는 그냥 sol1처럼 b2에 내림차순으로 정렬된 B를 넣어서 오름차순으로 정렬된 A와
# 곱하는 식으로 했지만 이것도 결국 B를 재배열한 값을 가지고 한거니까 제대로 풀지
# 않은 것 같은 기분이라 sol2를 만듬

# sol2
# B에 들어있는 값들의 인덱스를 값이 큰 순서대로 index_of_b에 넣고,
# A가 크기순으로 정렬된 리스트인 A2[i]의 값을 A[index_of_b[i]]에 넣어서
# A의 가장 작은 수가 B의 가장 큰 수와 곱해지도록 A의 값들을 재배열 함.

# sol3
# 생각해보니 재배열 하지 말라고 했지 꺼내서 쓰거나 지우지 말라는 말은 없었으므로
# a에 들어있는 값들중 가장 작은 값을 꺼내고, B에 들어있는 값들중 가장 큰 값을 꺼내서
# 곱한 값을 answer에 더해줌