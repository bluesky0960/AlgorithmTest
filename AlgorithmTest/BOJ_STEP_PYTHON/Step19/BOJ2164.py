# https://www.acmicpc.net/problem/2164
# 카드 2
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([i for i in range(1, n+1)])
while len(q) != 1:
    q.popleft()
    q.rotate(-1)

print(q.popleft())