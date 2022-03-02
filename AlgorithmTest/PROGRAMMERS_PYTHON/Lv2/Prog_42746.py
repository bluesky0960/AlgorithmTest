# https://programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수 

from itertools import permutations
def solution(numbers):
    newArr = [str(i) for i in numbers]
    newArr.sort(key = lambda x: x*3, reverse=True)
    answer = ''.join(newArr)
    
    return str(int(answer))