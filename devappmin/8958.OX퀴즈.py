loop = int(input())
for i in range(loop):
    ans = [0]
    s = input()
    for j in s:
        if j == 'O':
            ans.append(ans[len(ans) - 1] + 1)
        else:
            ans.append(0)
    print(sum(ans))