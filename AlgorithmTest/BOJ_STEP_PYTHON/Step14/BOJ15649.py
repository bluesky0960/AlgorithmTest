#https://www.acmicpc.net/problem/15649
import sys
import itertools
n, m = map(int, sys.stdin.readline().split())

a = [i for i in range(1, n+1)]

result = itertools.permutations(a, m)
b=[]
for i in result:
    b.append(str(i).replace('(','').replace(')','').replace(' ','').split(','))

for i in b:
    print(*i)
