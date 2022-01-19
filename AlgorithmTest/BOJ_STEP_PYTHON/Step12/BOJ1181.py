#https://www.acmicpc.net/problem/1181
import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(sys.stdin.readline())
lst = list(set(lst))

lst.sort()
lst.sort(key=lambda x: len(x))
print(''.join(lst))