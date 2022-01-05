# https://www.acmicpc.net/problem/11653

n = int(input())

prime = 2
while n != 1:
    if n % prime == 0:
        n = n/prime
        print(prime)
    else:
        prime += 1

""" 시간 초과
prime = []
prime_used = []

isPrime = True
if n != 1:
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                isPrime = False
                break
            isPrime = True
        if isPrime:
            prime.append(i)

for i in prime:
    count = 0
    while True:
        if n%i==0:
            n = n//i
            count += 1
        else:
            break
    prime_used.append(count)

for i in range(len(prime)):
    for j in range(prime_used[i]):
        print(prime[i])
"""