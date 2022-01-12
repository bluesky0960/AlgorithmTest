#https://www.acmicpc.net/problem/11050

def fact_n(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, k = map(int, input().split())
result = fact_n(n)/(fact_n(k) * fact_n(n-k))
print(int(result))