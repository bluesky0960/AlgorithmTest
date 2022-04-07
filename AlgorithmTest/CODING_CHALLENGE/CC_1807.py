# https://ktaivle-ai.moducoding.com/Question/1807/View/1
# 1로 만들기(초급)

import sys

n = int(sys.stdin.readline())

result = [0] * 30001

result[1] = 0

for i in range(2, n+1):
    result[i] = result[i-1] + 1
    if i % 2 == 0:
        result[i] = min([result[i], result[i//2] + 1])
    if i % 3 == 0:
        result[i] = min([result[i], result[i//3] + 1])
    if i % 5 == 0:
        result[i] = min([result[i], result[i//5] + 1])
    
    

print(result[n])