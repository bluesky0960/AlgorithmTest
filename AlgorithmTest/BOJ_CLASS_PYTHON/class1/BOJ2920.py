#https://www.acmicpc.net/problem/2920

n = map(int, input().split())

tmp = 0
count = 0
for i in n:
    if tmp == 0:
        tmp = i
    else:
        if tmp - i == 1:
            count += 1
        elif tmp - i == -1:
            count -= 1
        else:
            print('mixed')
            break
        tmp = i
if count == 7:
    print('descending')
elif count == -7:
    print('ascending')