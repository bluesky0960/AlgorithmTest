# https://www.acmicpc.net/problem/10872

def n_fac(n):
    if n==1:
        return 1
    else:
        return n * n_fac(n-1)

n = int(input())

if n == 0:
    print(1)
else:
    print(n_fac(n))