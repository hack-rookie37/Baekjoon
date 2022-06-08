n = int(input()) # 멀티탭의 개수 N
consent_num = sum([int(input()) for _ in range(n)])

print(consent_num - n + 1)