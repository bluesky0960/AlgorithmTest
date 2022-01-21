#https://www.acmicpc.net/problem/10814
import sys

n = int(sys.stdin.readline())

a = []
for i in range(n):
    a.append([i] + sys.stdin.readline().split())

a.sort(key=lambda x:(int(x[1]), x[0]))

for i in a:
    print(i[1], i[2])
