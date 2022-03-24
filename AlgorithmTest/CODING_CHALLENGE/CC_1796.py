# https://ktaivle-ai.moducoding.com/Question/1796/View/1
# 지방선거

import sys
from collections import defaultdict

n = int(sys.stdin.readline())

n_dict = defaultdict(int)

for _ in range(n):
    a = int(sys.stdin.readline())
    n_dict[a] += 1
n_dict = sorted(n_dict.items(), key=lambda x:(-x[1], x[0]))
print(n_dict[0][0])