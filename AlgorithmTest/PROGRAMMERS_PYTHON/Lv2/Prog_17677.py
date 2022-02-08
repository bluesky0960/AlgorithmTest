# https://programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스클러스터링

import re
import math
def solution(str1, str2):
    answer = 0
    str_1 = {}
    str_2 = {}
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 == str2:
        return 65536
    
    p = re.compile('[^a-z]')
    for i in range(len(str1) - 1):
        a = str1[i] + str1[i+1]
        m = p.search(a)
        if not m:
            if a not in str_1.keys():
                str_1[a] = 1
            else:
                str_1[a] += 1
                
    for i in range(len(str2) - 1):
        a = str2[i] + str2[i+1]
        m = p.search(a)
        if not m:
            if a not in str_2.keys():
                str_2[a] = 1
            else:
                str_2[a] += 1

    if len(str_1) == 0 or len(str_2) == 0:
        return 0
    
    k_1 = set(str_1.keys())
    k_2 = set(str_2.keys())
    
    uk = k_1 | k_2
    ik = k_1 & k_2
    
    u_c = 0
    for i in uk:
        if i in str_1.keys() and i in str_2.keys():
            if str_1[i] >= str_2[i]:
                u_c += str_1[i]
            else:
                u_c += str_2[i]
        else:
            if i in str_1.keys():
                u_c += str_1[i]
            else:
                u_c += str_2[i]
                
    i_c = 0
    for i in ik:
        if str_1[i] <= str_2[i]:
            i_c += str_1[i]
        else:
            i_c += str_2[i]
    
    answer = math.floor((i_c/u_c) * 65536)

    return answer