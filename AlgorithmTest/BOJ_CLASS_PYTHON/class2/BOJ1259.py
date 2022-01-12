#https://www.acmicpc.net/problem/1259

#자릿수 1개, 짝수개 홀수개

while True:
    n = input()
    if n == '0':
        break
    isPal = True
    for i in range(len(n)//2):
        if n[i] == n[-(i+1)]:
            continue
        else:
            isPal = False
            break

    if isPal:
        print('yes')
    else:
        print('no')