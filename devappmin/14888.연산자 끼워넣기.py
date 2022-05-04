import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

min_ans, max_ans = sys.maxsize, -sys.maxsize

def dfs(num, idx, pl, mi, mu, di):
    global min_ans, max_ans

    if idx == n:
        min_ans = min(min_ans, num)
        max_ans = max(max_ans, num)
        return

    if pl > 0:
        dfs(num + nums[idx], idx + 1, pl - 1, mi, mu, di)
    
    if mi > 0:
        dfs(num - nums[idx], idx + 1, pl, mi - 1, mu, di)

    if mu > 0:
        dfs(num * nums[idx], idx + 1, pl, mi, mu - 1, di)

    if di > 0:
        dfs(int(num / nums[idx]), idx + 1, pl, mi, mu, di - 1)
    

dfs(nums[0], 1, *operator)
print(max_ans, min_ans, sep="\n")