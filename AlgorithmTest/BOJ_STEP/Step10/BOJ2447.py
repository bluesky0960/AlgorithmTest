#https://www.acmicpc.net/problem/2447

def star(n, x):
    matrix = []
    if n == 3:
        return x
    else:
        for i in x:
            matrix.append(i*3)
        for i in x:
            matrix.append(i + ' ' * len(x) + i)
        for i in x:
            matrix.append(i*3)
        return star(n//3, matrix)
    

n = int(input())
x = ["***", "* *", "***"]
result = star(n, x)
for i in result:
    print(i)