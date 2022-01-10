#https://www.acmicpc.net/problem/1002

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    if dist==0 and r1==r2:
        print(-1)
    elif dist == r1+r2 or dist == abs(r1-r2):
        print(1)
    elif dist > abs(r1-r2) and dist < r1 + r2:
        print(2)
    else:
        print(0)