# https://ktaivle-ai.moducoding.com/Question/1799/View/1
# 무향 그래프 1

import sys

v, e = map(int, sys.stdin.readline().split())
mat = [[0]*v for _ in range(v)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    mat[a-1][b-1] = mat[b-1][a-1] = 1

for i in mat:
    print(*i)