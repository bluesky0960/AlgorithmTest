# https://ktaivle-ai.moducoding.com/Question/1794/View/1
# 우리반 아이큐왕은

import sys
from collections import defaultdict

n = int(sys.stdin.readline())

d = defaultdict(int)

for _ in range(n):
    name, iq = sys.stdin.readline().strip().split()
    d[name] = int(iq)

d = sorted(d.items(), key=lambda x:x[1], reverse=True)
for i in range(3):
    print(d[i][0])