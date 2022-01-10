#https://www.acmicpc.net/problem/1065

count = 0
n = int(input())
for i in range(1, n+1):
    if i < 100:
        count+=1
    else:
        str_i = str(i)
        if (int(str_i[0])-int(str_i[1]) == int(str_i[1])-int(str_i[2])):
            count+=1
print(count)