# https://ktaivle-ai.moducoding.com/Question/1795/View/1
# 전투력
import sys

n = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
length = len(tmp)
maxNum = 0
tmp.sort()
for i in range(length):
    if maxNum < tmp[i] * (length - i):
        maxNum = tmp[i] * (length-i)
print(maxNum)