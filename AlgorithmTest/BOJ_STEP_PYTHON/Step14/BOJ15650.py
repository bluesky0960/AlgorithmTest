#https://www.acmicpc.net/problem/15650
import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n+1)]
print(a)
for i in range(len(a)):
    st = str(a[i])
    cnt = 1
    for j in range(i+1, len(a)):
        if cnt < m:
            st+=(' ' + str(a[j]))
            print('st',st)
            j-=1
            cnt +=1
        else:
            cnt = 0
            