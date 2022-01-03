# https://www.acmicpc.net/problem/11022

n = int(input())

for i in range(n):
    a, b = input().split()
    print(f"Case #{i+1}: {int(a)} + {int(b)} = {int(a) + int(b)}")