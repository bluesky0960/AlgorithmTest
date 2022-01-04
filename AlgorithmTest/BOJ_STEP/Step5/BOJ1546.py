#https://www.acmicpc.net/problem/1546

n = int(input())
score = input().split()
score = list(map(int, score))
max_num = max(score)
sum = 0
for i in score:
    sum = sum + (i/max_num)*100
print(sum/len(score))
