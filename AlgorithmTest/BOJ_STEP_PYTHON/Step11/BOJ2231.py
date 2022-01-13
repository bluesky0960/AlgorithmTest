#https://www.acmicpc.net/problem/2231

"""
int(x)+int(x[0] + ... + int(x[len(x)]) = n)
"""
n = input()
flag=False
for i in range(int(n) - (9 * len(n)), int(n)):
    if i >= 0:
        result = i
        for j in range(len(str(i))):
            result += int(str(i)[j])
        if result == int(n):
            flag=True
            print(i)
            break
if not flag:
    print(0)