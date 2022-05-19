import re

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        tc = input()
        p = re.compile("(100+1+|01)+")

        if p.fullmatch(tc):
            print("YES")
        else:
            print("NO")
