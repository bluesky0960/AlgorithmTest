import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    name, score = sys.stdin.readline().strip().split()
    q.append((name, int(score)))
if n==1:
    print(q.popleft()[0])
    exit(0)

elif n%2!=0:
    n += 1
    q.append(('tmp', 0))

cnt = 0
tonument = deque()
tmp = []
while len(q)!=1:
    n1 = q.popleft()
    n2 = q.popleft()
    tmp.append(n1[0])
    if n2[0] != 'tmp':
        tmp.append(n2[0])
    q.append(n1) if n1[1] >= n2[1] else q.append(n2)
    cnt+=2
    if cnt == n:
        tonument.append(tmp)
        n //= 2
        cnt = 0
        tmp = []
tonument.append([q.popleft()[0]])

while tonument:
    print(*tonument.pop())