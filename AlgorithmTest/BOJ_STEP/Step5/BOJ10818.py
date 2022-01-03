# https://www.acmicpc.net/problem/10818

n = int(input())
a = []
a = input().split()

min = int(a[0])
max = int(a[0])

for i in range(n):
    if int(a[i]) < min:
        min = int(a[i])
    if int(a[i]) > max:
        max = int(a[i])

print(f"{min} {max}")