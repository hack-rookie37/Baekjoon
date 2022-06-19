import sys

left, right, shift = 0x2, 0x20, -1

def rol(i):
    s = i << 1
    o = (s & 0x100) >> 8
    s &= 0xff
    return o | s

def ror(i):
    o = i & 1
    o <<= 7
    s = i >> 1
    return o | s

def rotate(i, p):
    return rol(i) if p == -1 else ror(i)

gears = [int(sys.stdin.readline(), base=2) for _ in range(4)]

for _ in range(int(sys.stdin.readline())):
    num, direction = map(int, sys.stdin.readline().split())
    temp = direction * shift
    temp_gears = gears[:]
    num -= 1

    for i in range(num, 0, -1):
        if ( temp_gears[i] & left ) >> 1 == ( temp_gears[i - 1] & right ) >> 5:
            break
        
        gears[i - 1] = rotate(gears[i - 1], temp)
        temp *= shift

    temp = direction * shift

    for i in range(num, 3):
        if ( temp_gears[i] & right ) >> 5 == ( temp_gears[i + 1] & left ) >> 1:
            break
        
        gears[i + 1] = rotate(gears[i + 1], temp)
        temp *= shift
    
    gears[num] = rotate(gears[num], direction)

print(sum([(gears[x] >> 7) * (2 ** x) for x in range(4)]))

# N = 0, S = 1

# 10011101 00000001
# 00100000 00000010
