# https://www.acmicpc.net/problem/9020

maxNum = 10000 + 1

isPrime = [True] * maxNum
for i in range(2, maxNum):
    if isPrime[i]:
        for j in range(2*i, maxNum, i):
            isPrime[j] = False
print(isPrime)

t = int(input())

for _ in range(t):
    n = int(input())
    b = n//2

""" 시간 초과
def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    a = [i for i in range(3, n+1)]
    b = {}
    for i in a:
        if i not in b:
            if prime(i) and prime(n-i):
                b[abs(n-i-i)] = f"{n-i} {i}"
    print(b[min(b.keys())])
"""

""" 시간 초과
maxNum = 10000 + 1
a = [True for i in range(maxNum)]
b = []
for i in range(2, maxNum):
    if a[i]:
        b.append(i)
        for j in range(2*i, maxNum, i):
                a[j] = False
t = int(input())

for _ in range(t):
    
    n = int(input())
    d={}
    for i in b[::-1]:
        if n - i in b:
            d[abs(n - i - i)] = f"{i} {n-i}"
                
    print(d[min(d.keys())])
"""
#for idx, var in enumerate(a):
#    if idx != 0 and idx != 1 and var == True:
#        b.append(idx)

"""
t = int(input())

for i in range(t):
    n = int(input())
    c = {}
    for i in b[::-1]:
        if n - i in b:
            c[abs(n-i-i)] = [i, n-i]
    minKey = min(c.keys())
    print(str(c[minKey]).replace(',','').replace('[','').replace(']',''))
"""