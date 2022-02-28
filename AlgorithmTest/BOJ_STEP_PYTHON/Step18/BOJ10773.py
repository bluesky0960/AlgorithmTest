# https://www.acmicpc.net/problem/10773
# 제로

from sys import stdin

n = int(stdin.readline().strip())

s = []
for i in range(n):
    num = int(stdin.readline().strip())
    if num == 0 and s:
        s.pop()
    else:
        s.append(num)

print(sum(s))