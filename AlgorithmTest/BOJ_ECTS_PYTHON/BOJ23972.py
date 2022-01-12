#https://www.acmicpc.net/problem/23972

"""
(total - k) * n >= total
ntotal - nk >= total
-nk >= total - ntotal
-nk >= (1-n)total
-nk/(1-n) >= total

"""
import math
k, n = map(int, input().split())
if n==1:
    print(-1)
else:
    money = (n*k*(-1))//(1-n)
    if (n*k*(-1))%(1-n):
        money+=1
    print(money)

