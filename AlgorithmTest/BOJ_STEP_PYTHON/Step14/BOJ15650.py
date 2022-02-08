#https://www.acmicpc.net/problem/15650
import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n+1)]
nCr = list(itertools.combinations(a, m))

for i in nCr:
    print(*i)
