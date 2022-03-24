# https://ktaivle-ai.moducoding.com/Question/1797/View/1
# 무료급식

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dict_n = defaultdict(list)
for _ in range(n):
    age, name = sys.stdin.readline().strip().split()
    dict_n[int(age)].append(name)

dict_n = sorted(dict_n.items(), reverse=True)
for i in dict_n:
    for j in i[1]:
        print(j)