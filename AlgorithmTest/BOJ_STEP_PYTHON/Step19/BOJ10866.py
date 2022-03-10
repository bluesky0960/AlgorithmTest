# https://www.acmicpc.net/problem/10866
# 덱
import sys
from collections import deque

num = int(sys.stdin.readline())
q = deque()

for _ in range(num):
    com = sys.stdin.readline().strip()
    if com.startswith('push'):
        com, n = com.split(' ')
        if com.endswith('back'): q.append(int(n))
        elif com.endswith('front'): q.appendleft(int(n))
    elif com=='size': print(len(q))
    elif com=='empty': print(1) if len(q)==0 else print(0)
    else:
        if q:
            if com=='pop_front': print(q.popleft())
            if com=='pop_back': print(q.pop())
            if com=='front': print(q[0])
            if com=='back': print(q[-1])
        else:
            print(-1)