import sys

test_case = int(sys.stdin.readline())
nums = []

def dfs(statement, idx):

    if idx == len(nums):
        if eval(statement.replace(' ', '')) == 0:
            print(statement)
        return

    dfs(statement + ' ' + str(nums[idx]), idx + 1)
    dfs(statement + '+' + str(nums[idx]), idx + 1)
    dfs(statement + '-' + str(nums[idx]), idx + 1)


for _ in range(test_case):
    nums = [x for x in range(1, int(sys.stdin.readline()) + 1)]
    dfs('1', 1)
    print()