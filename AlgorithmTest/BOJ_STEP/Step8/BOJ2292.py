# https://www.acmicpc.net/problem/2292

num = int(input())

count = 1
a = 1
if num == 1:
    print(1)
else:
    while True:
        if a >= num:
            break
        else:
            a += 6 * count
            count += 1

    print(count)
