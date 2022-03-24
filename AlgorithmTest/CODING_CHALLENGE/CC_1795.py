# https://ktaivle-ai.moducoding.com/Question/1795/View/1
# 전투력
import sys

n = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
if len(tmp)-1 == 1:
    print(min(tmp)*2)
else:
    tmp.sort()
    print(tmp[1] * (len(tmp)-1))