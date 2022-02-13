#https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    p_dict = {}
    for i in participant:
        if i not in p_dict.keys():
            p_dict[i] = 1
        else:
            p_dict[i] += 1
    
    for i in completion:
        p_dict[i] -= 1
    
    for key, val in p_dict.items():
        if val == 1:
            answer = key
    return answer