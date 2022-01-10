#https://www.acmicpc.net/problem/1157

listAlpha = [0 for i in range(26)]

st = input().lower()

for i in st:
    listAlpha[ord(i)-97] += 1

max_num = max(listAlpha)
count = 0
max_idx = -1
for idx, var in enumerate(listAlpha):
    if var == max_num:
        count += 1
        if(count > 1):
            break
        else:
            max_idx = idx
if(count>1):
    print('?')
else:
    print(chr(max_idx+97).upper())