# https://www.acmicpc.net/problem/1874
# 스택 수열

from sys import stdin

n = int(stdin.readline().strip())
numArr = [int(stdin.readline().strip()) for _ in range(n)]
pre=0
stack=[]
tmp = []
for i in numArr:
    if pre < i:
        for j in range(pre+1, i+1):
            tmp.append(j)
            stack.append('+')
        pre = tmp.pop()
        stack.append('-')
    else:
        if tmp[-1] == i:
            tmp.pop()
            stack.append('-')
        else:
            break

if tmp:
    print('NO')
else:
    for i in stack:
        print(i)