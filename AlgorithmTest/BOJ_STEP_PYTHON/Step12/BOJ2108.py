#https://www.acmicpc.net/problem/2108

import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()    
print(int(round(sum(a)/n)))
print(a[n//2])

dict_a = {}
for i in a:
    if i not in dict_a.keys():
        dict_a[i] = 1
    else:
        dict_a[i] += 1
b = []
for key, value in dict_a.items():
    if value == max(dict_a.values()):
        b.append(key)
b.sort()
if len(b) == 1:
    print(b[0])
else:
    print(b[1])
print(a[n-1] - a[0])
