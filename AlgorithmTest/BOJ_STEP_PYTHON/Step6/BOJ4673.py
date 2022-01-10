#https://www.acmicpc.net/problem/4673

a = [0 for i in range(10000)]

def d(n):
    total = n
    n10000 = n//10000
    if n10000 != 0:
        n -= 10000*n10000
    n1000 = n//1000
    if n1000 != 0:
        n -= 1000*n1000
    n100 = n//100
    if n100 != 0:
        n -= 100*n100
    n10 = n//10
    if n10 != 0:
        n -= 10*n10
    n1 = n
    sum_num = total + n10000 + n1000 + n100 + n10 + n1
    if sum_num <= 10000:
        a[sum_num-1] = 1

for i in range(1, 10001):
    d(i)

for idx, var in enumerate(a):
    if var == 0:
        print(idx+1)