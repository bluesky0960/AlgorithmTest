# https://ktaivle-ai.moducoding.com/Question/1830/View/1
# 교도소(초급)

import sys
from itertools import combinations
v, e = map(int, sys.stdin.readline().split())
for i in range(1, v+1):
    print(list(combinations([i for i in range(1, v+1)], i))[0][0])
# if v==1 or e==1:
#     print(1)
# else:
#     tmp = [[] for _ in range(v+1)]
#     for _ in range(e):
#         a, b = map(int, sys.stdin.readline().split())
#         tmp[a].append(b)
#         tmp[b].append(a)
#     # ic = tmp[0] & tmp[1]
#     # print('ic', ic)
#     print(tmp)