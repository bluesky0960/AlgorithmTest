# https://www.acmicpc.net/problem/2884

time = 45

h, m = map(int, input().split())

m = m-45
if m < 0:
    if h-1 < 0:
        h = 23
    else:
        h = h-1
    m = 60 + m
print(f"{h} {m}")