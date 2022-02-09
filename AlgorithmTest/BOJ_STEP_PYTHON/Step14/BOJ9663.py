#https://www.acmicpc.net/problem/9663

import sys


n = int(sys.stdin.readline())
a = [0] * 15
count = 0

def isPromise(col):
    for i in range(col):
        if a[col] == a[i] or col-i == abs(a[col]-a[i]):
            return False
    
    return True

def dfs(col):
    if col == n:
        global count
        count+=1
        return
    
    for i in range(n):
        a[col] = i
        if isPromise(col):
            dfs(col + 1)



dfs(0)
print(count)