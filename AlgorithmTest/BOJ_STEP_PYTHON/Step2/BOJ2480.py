# https://www.acmicpc.net/problem/2480
# 주사위 세개

import sys
from collections import Counter

num = list(map(int, sys.stdin.readline().split(' ')))
num.sort(reverse=True)
dice = Counter(num).most_common()

if dice[0][1] == 3:
    print(10000 + dice[0][0] * 1000)
elif dice[0][1] == 2:
    print(1000 + dice[0][0] * 100)
else:
    print(dice[0][0] * 100)