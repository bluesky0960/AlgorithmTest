# https://ktaivle-ai.moducoding.com/Question/1818/View/1
# 바닥 공사 3

import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(31)]
dp[2] = 3
if n % 2 != 0:
    print(0)
else:
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) + 2
    print(dp[n])