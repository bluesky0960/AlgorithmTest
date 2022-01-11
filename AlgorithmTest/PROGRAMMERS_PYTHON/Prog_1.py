#https://programmers.co.kr/learn/courses/30/lessons/77484
#로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    
    correct = 0
    unknown = 0
    for i in lottos:
        if i in win_nums:
            correct += 1
        if i == 0:
            unknown += 1
    
    high = 7 - (correct + unknown)
    low = 7 - correct
    
    if low > 6:
        low = 6
    if high > 6:
        high = 6
    
    answer.append(high)
    answer.append(low)
    return answer