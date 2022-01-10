#https://www.acmicpc.net/problem/4344

testCase = int(input())
a = []
for i in range(testCase):
    st = input().split()
    st = list(map(int, st))
    avg = sum(st[1:])/st[0]
    
    count = 0
    for i in st[1:]:
        if i > avg:
            count = count + 1

    print("{:.3f}%".format(count/st[0] * 100))
    