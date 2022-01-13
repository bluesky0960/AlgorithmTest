#https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())

a = list(map(int, input().split()))

min_result = m
answer = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_a = a[i]+a[j]+a[k]
            if sum_a <= m and m-sum_a < min_result:
                min_result = m - (a[i] + a[j] + a[k])
                answer = a[i]+a[j]+a[k]
print(answer)