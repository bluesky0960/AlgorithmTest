#https://www.acmicpc.net/problem/7568

p = int(input())
a = []
b = []
for _ in range(p):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if i != j and a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            count += 1
    b.append(count+1)

print(*b)