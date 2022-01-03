# https://www.acmicpc.net/problem/2439

n = int(input())

for i in range(1, n+1):
    st = ""
    for j in range(1, n+1):
        if j <= n-i:
            st = st + " "
        else:
            st = st + "*"
    print(st)