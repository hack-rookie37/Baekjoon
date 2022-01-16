l, c = map(int, input().split()) # l = 암호의 자릿수, c = 암호로 사용했을 법한 문자의 종류
text = sorted(list(input().split())) #C개의 알파벳
# if c >= 15:
#     c = 15
# elif c<= 3:
#     c = 3
# text = text[0:c] # 알파벳 몇개가 입력되든 c개만 리스트에 저장

def pw_promising(arr):
    cnt_vow = 0
    for i in arr:
        if i in 'aeiou':
            cnt_vow += 1
    if cnt_vow >= 1 and l - cnt_vow >= 2: # 모음이 1개 이상, 자음이 2개 이상인지 확인
        print(''.join(arr))  #2
 
def dfs(idx, pw):
    if len(pw) == l: # 암호가 완성되면
        pw_promising(pw) # 유망한지(모음이 1개 이상, 자음이 2개 이상인지) 확인
        return
    if idx == c: # 주어진 문자를 모두 사용했을 때
     return
    pw.append(text[idx]) # 암호에 알파벳 하나 추가
    dfs(idx + 1, pw)
    pw.pop() # backtracking
    dfs(idx + 1, pw)
 
dfs(0, [])