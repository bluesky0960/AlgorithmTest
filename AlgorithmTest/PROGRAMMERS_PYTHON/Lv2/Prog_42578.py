#https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장
def solution(clothes):
    answer = 0
    c_dict = {}
    cnt = 1
    for i in clothes:
        if i[1] not in c_dict.keys():
            c_dict[i[1]] = 1
        else:
            c_dict[i[1]] += 1
    
    for i in c_dict.values():
        cnt *= (i+1)
    
    answer = cnt-1
    return answer
    

# def dfs(num, start):
#     global combo
#     global c_dict
#     global cnt
#     if len(combo) == num:
#         sum_c = 1
#         for com in combo:
#             sum_c *= com[1]
#         cnt+=sum_c
#         return
    
#     for key, val in list(c_dict.items())[start:]:
#         if (key, val) not in combo:
#             combo.append((key, val))
#             dfs(num, start+1)
#             combo.pop()
    # for key in list(c_dict.keys())[start:]:
    #     if key not in combo:
    #         for i in range(len(c_dict[key])):
    #             combo.append(key)
    #             dfs(num, start+1)
    #             combo.pop()