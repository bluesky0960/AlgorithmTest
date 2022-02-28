# https://www.acmicpc.net/problem/1874
# 스택 수열

from sys import stdin

n = int(stdin.readline().strip())

num = [i for i in range(1, n+1)]
tmp = []
pre = 1
for i in range(n):
    num = int(stdin.readline().strip())
    for j in range(pre, num):
        tmp.append(j)

    pre = num
