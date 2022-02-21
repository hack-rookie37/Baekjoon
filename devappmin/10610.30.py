found = sorted(list(map(int, input())), reverse=True)
print(int(''.join(map(str, found))) if 0 in found and not sum(found) % 3 else -1)