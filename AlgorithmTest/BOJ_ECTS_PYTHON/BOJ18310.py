#https://www.acmicpc.net/problem/18310
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
if len(a)%2==0:
    print(a[len(a)//2-1])
else:
    print(a[len(a)//2])