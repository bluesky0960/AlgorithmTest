# https://www.acmicpc.net/problem/1978

t = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    if i > 1:
        err = False
        for j in range(2, i):
            if i%j == 0:
                err = True     
        if not err:
            count += 1
print(count)
