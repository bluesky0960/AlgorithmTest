# https://programmers.co.kr/learn/courses/30/lessons/43164#
# 여행경로

from collections import defaultdict
def solution(tickets):
    answer = []
    stack = []
    c_dict = defaultdict(list)
    
    for key, val in tickets:
        c_dict[key].append(val)
    print(c_dict)
    
    stack.append('ICN')
    while stack:
        tmp = stack[-1]
        
        if not c_dict[tmp]:
            answer.append(stack.pop())
        else:
            c_dict[tmp].sort(reverse=True)
            stack.append(c_dict[tmp].pop())
    answer.reverse()
    return answer