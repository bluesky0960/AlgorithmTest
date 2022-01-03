#https://www.acmicpc.net/problem/1110

count = 0
n = input()

if len(n) == 1:
    n = "0" + n

a = n[0]
b = n[1]

while 1:
    c = int(a) + int(b)
    c = str(c)
    d = b + c[len(c)-1]
    if(d == n):
        count+=1
        break
    else:
        count+=1

    a = d[0]
    b = d[1]
    d = ""

print(count)