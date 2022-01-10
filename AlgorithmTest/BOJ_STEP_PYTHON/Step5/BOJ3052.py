#https://www.acmicpc.net/problem/3052

n = []
a = []
for i in range(10):
    n.append(int(input()))

for i in n:
    a.append(i%42)

a = set(a)
print(len(a))