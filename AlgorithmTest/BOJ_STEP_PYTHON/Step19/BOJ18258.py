# https://www.acmicpc.net/problem/18258
# 큐 2
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
q = deque()
for i in range(n):
    com = sys.stdin.readline().strip()
    if com.startswith('push'):
        num = int(com.split(' ')[1])
        q.append(num)
    elif q:
        if com=='pop':
            print(q.popleft())
        elif com=='size':
            print(len(q))
        elif com=='empty':
            print(0)
        elif com=='front':
            print(q[0])
        elif com=='back':
            print(q[-1])
    else:
        if com=='size':
            print(0)
        elif com=='empty':
            print(1)
        else:
            print(-1)