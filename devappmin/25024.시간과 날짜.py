for _ in range(int(input())):
    a, b = map(int, input().split())
    print("Yes" if a < 24 and b < 60 else "No", end=" ")
    if a in [1, 3, 5, 7, 8, 10, 12] and 0 < b < 32:
        print("Yes")
    elif a in [4, 6, 9, 11] and 0 < b < 31:
        print("Yes")
    elif a == 2 and 0 < b < 30:
        print("Yes")
    else:
        print("No")
