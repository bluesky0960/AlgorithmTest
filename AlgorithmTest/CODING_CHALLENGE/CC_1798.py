# https://ktaivle-ai.moducoding.com/Question/1798/View/1
# 사전만들기(초급)

import sys
from collections import defaultdict
n = int(sys.stdin.readline())
d = defaultdict(list)
for _ in range(n):
    name = sys.stdin.readline().strip()
    d[name].append(len(name))
    d[name].append(name)
d = sorted(d.items(), key=lambda x: (x[1][0], x[1][1]))
for i in d:
    print(i[0])