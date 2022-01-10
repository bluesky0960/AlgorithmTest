#https://www.acmicpc.net/problem/4153

while True:
    tri = list(map(int, input().split()))

    c = max(tri)
    if c == 0:
        break

    c2 = c**2

    for i in tri:
        if i != c:
            c2 -= (i**2)

    if c2 == 0:
        print("right")
    else:
        print("wrong")