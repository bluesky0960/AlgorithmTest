# https://www.acmicpc.net/problem/2525
# 오븐 시계
import sys
h, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

h += t//60
m += t%60

if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24
print(h, m)