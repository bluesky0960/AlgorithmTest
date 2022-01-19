#https://www.acmicpc.net/problem/11650

n = int(input())
a = []
for _ in range(n):
    b, c = map(int, input().split())
    a.append((b,c))

a.sort(key=lambda x:(x[0], x[1]))

for i in a:
    print(i[0], i[1])