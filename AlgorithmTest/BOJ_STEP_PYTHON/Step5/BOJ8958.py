#https://www.acmicpc.net/problem/8958

n = int(input())

for i in range(n):
    count = 0
    sum = 0
    test = input()
    for i in test:
        if i == "X":
            count = 0
        else:
            count = count + 1
            sum = sum + count
    print(sum)