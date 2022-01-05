#https://www.acmicpc.net/problem/2839

total = int(input())

kg5 = total//5

while True:
    last = total - kg5 * 5
    kg3 = last // 3
    last -= (kg3 * 3)

    if last == 0:
        print(kg5 + kg3)
        break
    if kg5 == 0 and last != 0:
        print(-1)
        break
    kg5 -= 1
