# https://www.acmicpc.net/problem/2438

n = int(input())

for i in range(1, n+1):
    st = ""
    for j in range(0, i):
        st = st + "*"
    print(st)