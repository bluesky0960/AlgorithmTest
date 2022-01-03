# https://www.acmicpc.net/problem/10950

testCase = int(input())

c = list()

for i in range(testCase):
    a, b = input().split()
    a = int(a)
    b = int(b)
    c.append(a+b)

for i in range(testCase):
    print(c[i])
