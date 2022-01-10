#https://www.acmicpc.net/problem/3009

dic_x = {}
dic_y = {}
for _ in range(3):
    x, y = map(int, input().split())
    
    if x not in dic_x.keys():
        dic_x[x] = 1
    else:
        dic_x[x] += 1
    if y not in dic_y.keys():
        dic_y[y] = 1
    else:
        dic_y[y] += 1

for key, value in dic_x.items():
    if value == 1:
        x = key

for key, value in dic_y.items():
    if value == 1:
        y = key
print(f"{x} {y}")