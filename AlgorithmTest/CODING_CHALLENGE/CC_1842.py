# https://ktaivle-ai.moducoding.com/Question/1842/View/1
# 경기가 끝난 후에(중급)

import sys

n = int(sys.stdin.readline())
a = [0 for _ in range(n+1)]
# n+1이 홀수 일 때
# f(n+1) = f(n) * (n+1) - 1

# n+1이 짝수 일 때
# f(n+1) = f(n) * (n+1) + 1

a[1] = 1
a[2] = 1

for i in range(3, n+1):
    if i%2==0:
        a[i] = (a[i-1] * i + 1)%10007
    else:
        a[i] = (a[i-1] * i - 1)%10007

print(a[n])