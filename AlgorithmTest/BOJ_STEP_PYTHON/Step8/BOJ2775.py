#https://www.acmicpc.net/problem/2775

testCase = int(input())

for i in range(testCase):
    list_base = [i for i in range(1, 15)]
    list_new = []
    k = int(input())
    n = int(input())
    for j in range(k):
        for l in range(n):
            if l-1 >= 0:
                list_new.append(list_new[l-1] + list_base[l])
            else:
                list_new.append(1)
        list_a = list_b
        list_b = []
    print(list_a[n-1])