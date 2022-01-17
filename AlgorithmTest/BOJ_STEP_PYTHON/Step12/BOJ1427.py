#https://www.acmicpc.net/problem/1427

n = input()
a = []
for i in n:
    a.append(int(i))

a.sort(reverse=True)
for i in a:
    print(i, end='')
