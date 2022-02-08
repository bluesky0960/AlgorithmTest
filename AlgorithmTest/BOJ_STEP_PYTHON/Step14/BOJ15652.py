#https://www.acmicpc.net/problem/15652
import sys
n, m = map(int, sys.stdin.readline().split())

s=[]

def dfs(num):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(num, n+1):
        s.append(i)
        dfs(i)
        s.pop()
        

dfs(1)