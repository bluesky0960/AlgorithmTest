# https://www.acmicpc.net/problem/1316

testCase = int(input())
count = 0
for i in range(testCase):
    st = input()
    a = []
    curAlpha = ""
    isCon = True
    for i in st:
        if i not in a and i != curAlpha:
            curAlpha = i
            a.append(i)
        
        if i in a and i != curAlpha:
            isCon = False
            break
    if isCon:
        count += 1

print(count)