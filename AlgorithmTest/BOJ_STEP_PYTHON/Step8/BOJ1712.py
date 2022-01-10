#https://www.acmicpc.net/problem/1712

a, b, b2 = map(int, input().split())

if b >= b2:
    print(-1)
else:
    bx = b2 - b
    count = a // bx + 1
    print(count)