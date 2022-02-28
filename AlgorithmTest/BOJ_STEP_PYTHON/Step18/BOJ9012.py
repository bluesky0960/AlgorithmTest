# https://www.acmicpc.net/problem/9012
# 괄호

from sys import stdin

n = int(stdin.readline().strip())

for i in range(n):
    s = stdin.readline().strip()
    s = list(s)
    isVPS = True
    if len(s)%2 == 0:
        a, b = 0, 0
        while s:
            str1 = s.pop()
            if str1 == ')':
                a+=1
            else:
                b+=1
            
            if a < b:
                isVPS = False
                break
        if a != b:
            isVPS = False
    else:
        isVPS = False
    
    if isVPS:
        print('YES')
    else:
        print('NO')