# https://www.acmicpc.net/problem/1021
# 회전하는 큐
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])
num = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in num:
    while q[0] != i:
        if q.index(i) <= len(q)//2:
            q.rotate(-1)
            cnt+=1
        else:
            q.rotate(1)
            cnt+=1
    q.popleft()
print(cnt)
    