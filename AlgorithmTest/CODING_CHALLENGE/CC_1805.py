# https://ktaivle-ai.moducoding.com/Question/1805/View/1
# 컴퓨터 학원

# a[1] = 3 = 2 + 1
# a[2] = 7 = 4 + 3
# a[3] = 17 = 6 + 8 + 3
# a[4] = 41  = 8 + 18 + 12 + 3
# a[5] = 105 = 10 + 42 + 34 + 16 + 3
# a[n] = a[n-1] * 2 + 2(n-1) - 1

import sys

a = [0] * 10001

n = int(sys.stdin.readline())

a[1] = 3


for i in range(2, n+1):
    a[i] = a[i-1] * (-1) + 10

print(int(a[n])) 