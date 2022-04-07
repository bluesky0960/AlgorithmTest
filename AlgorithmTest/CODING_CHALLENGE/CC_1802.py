# https://ktaivle-ai.moducoding.com/Question/1802/View/1#1
# 바닥공사 2(초급)

import sys

f = [0] * 1001

n = int(sys.stdin.readline())

f[1] = 1
for i in range(2, n+1):
    if i%2==0:
        f[i] = (2*f[i-1] + 1)%796796
    else:
        f[i] = (2*f[i-1] - 1)%796796
print(f[n])