d, h, w = map(int,input().split()) # TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W
r = d / (h ** 2 + w ** 2) ** 0.5
print(int(h * r), int(w * r))