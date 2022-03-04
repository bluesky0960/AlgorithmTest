# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기

import sys
from itertools import permutations

n = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, div = map(int, sys.stdin.readline().split())

tmp = ['+']*plus + ['-']*minus + ['*']*multi + ['%']*div
tmp_p = list(permutations(tmp, len(tmp)))

answer=[]
for com in tmp_p:
    result=numArr[0]
    for i in range(1, n):
        if com[i-1]=='+':
            result+=numArr[i]
        elif com[i-1]=='-':
            result-=numArr[i]
        elif com[i-1]=='*':
            result*=numArr[i]
        elif com[i-1]=='%':
            result = abs(result)//numArr[i] * (-1) if result < 0 else result//numArr[i]
    answer.append(result)
answer.sort()
print(answer[-1])
print(answer[0])