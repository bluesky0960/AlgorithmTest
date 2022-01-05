# https://www.acmicpc.net/problem/2581
m = int(input())
n = int(input())

isPrime = True
firstNum = 0
sumNum = 0
for i in range(m, n+1):
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                isPrime = False
                break
            isPrime = True
        if isPrime:
            if firstNum == 0:
                firstNum = i
            sumNum += i
if sumNum == 0:
    print(-1)
else:
    print(sumNum)
    print(firstNum)