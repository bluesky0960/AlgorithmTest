#https://www.acmicpc.net/problem/18406

n = input()
count = 0
score=0
isOn = False
for i in n:
    if isOn:
        score -= int(i)
    else:
        score += int(i)
    
    count+=1
    if count == len(n)//2:
        isOn = True
if score == 0:
    print("LUCKY")
else:
    print("READY")