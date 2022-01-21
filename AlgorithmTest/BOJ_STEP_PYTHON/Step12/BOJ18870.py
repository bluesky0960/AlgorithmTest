#https://www.acmicpc.net/problem/18870
import sys
n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
aSort = sorted(a)

dic={}
cnt = 0
for i in aSort:
    if i not in dic.keys():
        dic[i] = cnt
        cnt+=1

for i in a:
    print(dic[i], end=' ')