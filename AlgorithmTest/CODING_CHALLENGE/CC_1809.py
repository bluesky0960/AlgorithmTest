# https://ktaivle-ai.moducoding.com/Question/1809/View/1
# 게릴라 전투

import sys

n = int(sys.stdin.readline())
enemy = [int(sys.stdin.readline()) for _ in range(n)]
s, c = map(int, sys.stdin.readline().split())
enemy = [(i-s) for i in enemy]
cnt = len(enemy)
for i in enemy:
    if i > 0:
        while True:
            i -= c
            cnt += 1
            if i <= 0:
                break
print(cnt)