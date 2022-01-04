print(ord('a'))
print(ord('z'))

string = input()
listAlpha = [-1 for i in range(26)]
for idx, var in enumerate(string):
    if listAlpha[ord(var)-97] == -1:
        listAlpha[ord(var)-97] = idx

print(str(listAlpha).replace(',', '').replace('[', '').replace(']',''))