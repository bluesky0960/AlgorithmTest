#https://www.acmicpc.net/problem/1436

a = []

n = int(input())

num = 666
while len(a) != n:
    if '666' in str(num):
        a.append(num)
    num+=1
print(a[n-1])