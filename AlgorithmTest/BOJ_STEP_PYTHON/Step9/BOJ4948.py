#https://www.acmicpc.net/problem/4948

# 에라토스테네스 체를 이용
maxNum = 123456 * 2 + 1
a = [True for i in range(maxNum)]
for i in range(2, int(maxNum**0.5) + 1):
    if a[i]:
        for j in range(2*i, maxNum, i):
            a[j] = False

while True:
    n = int(input())
    if n==0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if a[i]:
            cnt +=1
    print(cnt)

"""
 시간 초과
while True:
    n = int(input())
    if n==0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if Prime(i):
            cnt+=1
    print(cnt)
"""