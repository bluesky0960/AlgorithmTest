# https://www.acmicpc.net/problem/2562

idx = 0
max = 0
for i in range(9):
    n = int(input())
    if max < n:
        idx = i
        max = n
print(max)
print(idx+1)