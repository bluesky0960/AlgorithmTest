# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

from sys import stdin

special = ['(',')','[',']']
while True:
    isVPS = True
    str1 = stdin.readline()
    if str1 == '.\n':
        break
    s = [i for i in str1 if i in special]
    tmp = []
    for i in s:
        if i == '(' or i == '[':
            tmp.append(i)
        else:
            if i == ')':
                if tmp and tmp[-1] == '(':
                    tmp.pop()
                else:
                    isVPS=False
                    break
            elif i == ']':
                if tmp and tmp[-1] == '[':
                    tmp.pop()
                else:
                    isVPS=False
                    break
    if isVPS and not tmp:
        print('yes')
    else:
        print('no')