#https://www.acmicpc.net/problem/1929
import math
m, n = map(int, input().split())

isPrime = True
for i in range(m, n+1):
    if i> 1:
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                isPrime = False
                break
            isPrime = True
        if isPrime:
            print(i)