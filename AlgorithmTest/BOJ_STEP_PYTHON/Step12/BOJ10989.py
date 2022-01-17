#https://www.acmicpc.net/problem/10989
import sys

a = [0] * 10001

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    a[num] += 1

for i in range(10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)