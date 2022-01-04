# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

m = a*b*c
m = str(m)
l = [0,0,0,0,0,0,0,0,0,0]
for i in m:
    if i=="0":
        l[0] = l[0] + 1
    elif i=="1":
        l[1] = l[1] + 1
    elif i=="2":
        l[2] = l[2] + 1
    elif i=="3":
        l[3] = l[3] + 1
    elif i=="4":
        l[4] = l[4] + 1
    elif i=="5":
        l[5] = l[5] + 1
    elif i=="6":
        l[6] = l[6] + 1
    elif i=="7":
        l[7] = l[7] + 1
    elif i=="8":
        l[8] = l[8] + 1
    else:
        l[9] = l[9] + 1

for i in l:
    print(i)