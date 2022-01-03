#https://www.acmicpc.net/problem/2588
a = input()
b = input()

int_a = int(a)

result1 = int_a * int(b[2])
result2 = int_a * int(b[1])
result3 = int_a * int(b[0])

print(result1)
print(result2)
print(result3)

print(result3*100 + result2*10 + result1)