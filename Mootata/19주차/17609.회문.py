def check(string, start, end): # 유사회문인지 확인
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def palindrome(string, start, end): # 회문인지 확인
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            if check(string, start + 1, end) or check(string, start, end - 1): # 다른 글자를 제외한 나머지는 서로 같은지 확인
                return 1
            else:
                return 2
    return 0

for t in range(int(input())):
    string = list(input().strip())
    print(palindrome(string, 0, len(string) - 1))