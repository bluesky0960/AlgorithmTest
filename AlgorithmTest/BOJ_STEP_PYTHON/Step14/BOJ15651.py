#https://www.acmicpc.net/problem/15651
import sys

s = []
n, m = map(int, sys.stdin.readline().split())

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(1, n+1):
        # 첫 수 넣기
        s.append(i)
        dfs()
        # 첫 수를 제외한 마지막 수 pop
        s.pop()

dfs()
