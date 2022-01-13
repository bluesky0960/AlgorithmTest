#https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())

n2 = n-8+1
m2 = m-8+1

w = 'WBWBWBWB'
b = 'BWBWBWBW'
a = []
change = []
for _ in range(n):
    a.append(input())

for i in range(n2):
    for j in range(m2):
        count = 0
        for k in range(i, 8+i):
            for l in range(j, 8+j):
                print('a[k] ', k , a[k])
                print('a[k][j]: ', a[k][j])
                if a[k][j] == 'W':
                    if a[k][l] != w[l-j]:
                        count+=1
                elif a[k][j] == 'B':
                    if a[k][l] != b[l-j]:
                        count+=1
        change.append(count)
print(change)