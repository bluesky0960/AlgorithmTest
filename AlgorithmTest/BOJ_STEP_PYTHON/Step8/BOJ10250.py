#https://www.acmicpc.net/problem/10250

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    if n%h == 0:
        print("{0:}{1:02d}".format(h, n//h))
    else:
        print("{0:}{1:02d}".format(n%h, n // h + 1))