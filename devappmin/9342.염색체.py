import re

for _ in range(int(input())):
    m = re.fullmatch(r'[A-F]?A*F*C*[A-F]?', input())
    print("Infected!" if m else "Good")