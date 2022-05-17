# https://ktaivle-ai.moducoding.com/Question/1815/View/1
# 동전 줍기

import sys

n = int(sys.stdin.readline())
a = []
idx = 0
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

cnt = a[0][idx]
for i in range(1, n):
    if a[i][idx] >= a[i][idx + 1]:
        cnt += a[i][idx]
    else:
        cnt += a[i][idx+1]
    idx += 1
print(cnt)