#https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

if abs(x - w) >= x:
    min_x = x
else:
    min_x = abs(x - w)

if abs(y - h) >= y:
    min_y = y
else:
    min_y = abs(y - h)

print(min_x if min_x <= min_y else min_y)