#https://www.acmicpc.net/problem/1712

a, b, price = map(int, input().split())
count = 1
while True:
    
    if (price*count) >= (a+(b*count)):
        break
    count += 1

print(count+1)