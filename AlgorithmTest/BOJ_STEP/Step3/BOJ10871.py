# https://www.acmicpc.net/problem/10871

n, x = input().split()

n = int(n)
x = int(x)

A = input().split()
st = ""
for i in range(n):
    if x > int(A[i]):
        st = st + A[i]
        if n-i != 0:
            st = st + " "
print(st)