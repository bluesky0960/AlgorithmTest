# https://www.acmicpc.net/problem/1966
# 프린터 큐

import sys
from collections import deque

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    n, pos = map(int, sys.stdin.readline().split())
    num = [i for i in range(n)]
    answer_num = num[pos]
    
    imp = list(map(int, sys.stdin.readline().split()))
    sort_imp = sorted(imp, reverse=True)

    q = deque([[i, j] for i, j in zip(num, imp)])
    idx, cnt = 0, 0
    while q:
        if sort_imp[idx] != q[0][1]:
            q.rotate(-1)
        else:
            q_num = q.popleft()
            if answer_num == q_num[0]:
                print(idx + 1)
                break
            idx += 1