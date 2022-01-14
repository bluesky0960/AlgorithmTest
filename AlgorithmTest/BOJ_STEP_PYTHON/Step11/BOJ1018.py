#https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())

n2 = n-8+1
m2 = m-8+1

w = 'WBWBWBWB'
b = 'BWBWBWBW'
a = []
change = []
for _ in range(n):
    a.append(input())

for i in range(n2):
    for j in range(m2):
        isW = True
        for _ in range(2):
            isW = not isW
            count = 0
            for k in range(i, 8+i):
                for l in range(j, 8+j):
                    if isW:
                        if(k-i)%2==0:
                            if a[k][l] != w[l-j]:
                                count+=1
                        else:
                            if a[k][l] != b[l-j]:
                                count+=1
                        
                    else:
                        if(k-i)%2==0:
                            if a[k][l] != b[l-j]:
                                count+=1
                        else:
                            if a[k][l] != w[l-j]:
                                count+=1
            change.append(count)
                        
print(min(change))