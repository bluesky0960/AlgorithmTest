# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])
answer = []
while q:
    q.rotate(-(k))
    answer.append(q.pop())
print('<' + str(answer).replace('[','').replace(']','')+'>')