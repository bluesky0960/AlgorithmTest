# https://ktaivle-ai.moducoding.com/Question/1799/View/1
# 무향 그래프 2

import sys
from collections import defaultdict
v, e = map(int, sys.stdin.readline().split())

dict_e = {i:[] for i in range(1, v+1)}

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    dict_e[a].append(b)
    dict_e[b].append(a)

for key, val in dict_e.items():
    print(f'{key}: ', end='')
    print(*val)